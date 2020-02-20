from flask import Flask
from flask_restful import Api
# from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from db import db

from resources.user import User, UserRegistration, UserLogin
from resources.position import Portfolio, Position

# Init app
app = Flask(__name__)
api = Api(app)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/tickr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JSON Web Token
app.config['SECRET_KEY'] = 'thisissecret'

# Init db
db.init_app(app)
# ma = Marshmallow(app) 
jwt = JWTManager(app)

@app.before_first_request
def create_tables():
    db.create_all()

# # User Schema
# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'email', 'password')

# # Init schema
# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

api.add_resource(User, "/user")
api.add_resource(UserRegistration, "/registration")
api.add_resource(UserLogin, "/login")
api.add_resource(Position, '/position/<string:ticker>')
api.add_resource(Portfolio, '/portfolio')

# Run Server
if __name__ == '__main__':
    app.run(debug=True)