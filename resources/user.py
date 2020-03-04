from flask import request, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models.user import UserModel, user_schema, users_schema

class User(Resource):
  def get(self):  
    users = UserModel.query.all()
    result = users_schema.dump(users)
    return jsonify(result)
  
  def post(self):
    pass
  
  def update(self):
    pass
  
  def delete(self):
    pass

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()

        if UserModel.find_by_email(data['email']):
            return {'message': 'User already exists'}, 409

        hashed_password = generate_password_hash(data['password'], method='sha256')
    
        new_user = UserModel(
            email=data['email'],
            password=hashed_password
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = current_user.id)
            refresh_token = create_refresh_token(identity = current_user.id)
            
            return {
                'message': 'User {} was created'.format(data['email']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }, 201
        except:
            return {'message': 'Something went wrong'}, 500

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        current_user = UserModel.find_by_email(data['email'])

        if not current_user:
            return {'message': 'User not found'}, 401
        
        if check_password_hash(current_user.password, data['password']):
            access_token = create_access_token(identity = current_user.id)
            refresh_token = create_refresh_token(identity = current_user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}, 401
