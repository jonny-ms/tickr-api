from flask import request
from flask_restful import Resource
from flask_jwt_extended import (jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models.position import PositionModel

class Position(Resource):
  @jwt_required
  def get(self, ticker):
    return {'message': 'Success: {} position requested'.format(ticker)}

  @jwt_required
  def post(self, ticker):
    data = request.get_json()

    new_position = PositionModel(
      ticker = data['ticker'],
      amount = data['amount'],
      price = data['price'],
      date = data['date'],
      user_id = get_jwt_identity()
    )

    try:
        new_position.save_to_db()
        
        return {'message': f'Position created: {new_position.amount} shares of {new_position.ticker} at {new_position.price} on {new_position.date}. User id: {new_position.user_id}'}
    except:
        return {'message': 'Something went wrong'}, 500


  @jwt_required  
  def update(self):
    pass
  
  @jwt_required
  def delete(self):
    pass

class Portfolio(Resource):
  @jwt_required
  def get(self):
    pass