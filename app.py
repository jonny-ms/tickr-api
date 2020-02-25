from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from db import db, ma
import os

from resources.user import User, UserRegistration, UserLogin
from resources.position import Portfolio, Position
from resources.stock import Stock
from resources.watched import Watched, Watchlist

# Init app
app = Flask(__name__)
api = Api(app )

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('CLEARDB_DATABASE_URL', 'mysql+pymysql://root:password@localhost/tickr')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JSON Web Token
app.config['SECRET_KEY'] = 'thisissecret'

ma.init_app(app)
jwt = JWTManager(app)

api.add_resource(User, "/user")
api.add_resource(UserRegistration, "/registration")
api.add_resource(UserLogin, "/login")
api.add_resource(Position, '/position/<int:_id>')
api.add_resource(Portfolio, '/portfolio')
api.add_resource(Stock, '/stock/<string:ticker>')
api.add_resource(Watched, '/watch/<string:ticker>')
api.add_resource(Watchlist, '/watchlist')

# Run Server
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)