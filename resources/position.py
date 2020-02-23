from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models.position import PositionModel, position_schema, portfolio_schema
import datetime

class Position(Resource):
  @jwt_required
  def get(self, _id):
    position = PositionModel.query.get(_id)
    result = position_schema.dump(position)
    return jsonify(result)

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
    user_id = get_jwt_identity()
    portfolio = PositionModel.query.filter_by(user_id=user_id).all()
    result = portfolio_schema.dump(portfolio)
    return jsonify(result)