from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models.watched import WatchedItemModel, watched_item_schema, watchlist_schema

class Watched(Resource):
  @jwt_required
  def get(self, ticker):
    pass

  @jwt_required
  def post(self, ticker):
    if WatchedItemModel.query.filter_by(user_id=get_jwt_identity(), ticker=ticker).first():
      return {'message': f'Already watching {ticker}'}, 400

    new_watched_item = WatchedItemModel(
      ticker = ticker,
      user_id = get_jwt_identity()
    )

    try:
      new_watched_item.save_to_db()
    except:
      return {'message': 'Something went wrong'}, 500

    return {'message': f'Watching: {new_watched_item.ticker}. User id: {new_watched_item.user_id}'}, 201
  
  @jwt_required
  def delete(self, ticker):
    watched_item = WatchedItemModel.query.filter_by(ticker=ticker).first()

    if watched_item:
      watched_item.delete_from_db()
      return {'message': f'No longer watching: {ticker}.'}

    return {'message': 'Item not found'}, 404


class Watchlist(Resource):
  @jwt_required
  def get(self):
    watchlist = WatchedItemModel.query.filter_by(user_id=get_jwt_identity()).all()
    result = watchlist_schema.dump(watchlist)
    tickers = []
    for r in result:
      tickers.append(r['ticker'])
    return jsonify(tickers)