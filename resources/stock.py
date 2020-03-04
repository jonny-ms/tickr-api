from flask import request
from flask_restful import Resource
import requests
import os
import aiohttp
import asyncio
from flask_jwt_extended import (jwt_optional, get_jwt_identity, jwt_required)
from models.watched import WatchedItemModel

api_key = os.environ.get('WORLD_TRADING_API_KEY')

class Stock(Resource):
  @jwt_optional
  def get(self, ticker):
    # make api call:
    # get realtime quote for header
    # get intraday data for chart
    # do I get data for all scopes of chart? ie. intraday for 1 week, historical data up to 5 years?
    # do I make a db query to see if stock is in watchlist and send boolean as part of response 

    stock_payload = { 
      'symbol': ticker,
      'api_token': api_key
      }
    intraday_payload = { 
      **stock_payload,
      'interval': '5',
      'range': '1',
      }
    intraweek_payload = { 
      **stock_payload,
      'interval': '60',
      'range': '5',
      }
    intraweek_payload = { 
      **stock_payload,
      'interval': '60',
      'range': '5',
      }



    async def fetch(session, req):
      (url, params) = req
      async with session.get(url, params=params) as response:
        return await response.json()
    
    async def api_call():
      reqs = [
        ('https://api.worldtradingdata.com/api/v1/stock', stock_payload),
        ('https://intraday.worldtradingdata.com/api/v1/intraday', intraday_payload)
        # ('https://api.worldtradingdata.com/api/v1/history', stock_payload)
        ]
      tasks = []
      async with aiohttp.ClientSession() as session:
        for req in reqs:
          tasks.append(fetch(session, req))
        responses = await asyncio.gather(*tasks)
        return responses

    # If logged in, query db to see if stock is being watched
    watched = False

    if get_jwt_identity():
      if WatchedItemModel.query.filter_by(user_id=get_jwt_identity(), ticker=ticker).first():
        watched = True
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    r1, r2 = loop.run_until_complete(api_call())

    return {'watched': watched, 'quote': r1['data'], 'intraday': r2['intraday']}


class Stocks(Resource):
  def get(self):
    args = request.args
    tickers = args['tickers']

    payload = { 
      'symbol': tickers,
      'api_token': api_key
      }

    r = requests.get('https://api.worldtradingdata.com/api/v1/stock', params=payload)

    return r.json()