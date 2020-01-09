from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JSON Web Token
app.config['SECRET_KEY'] = 'thisissecret'

# Init db
db = SQLAlchemy(app)

# Init db
ma = Marshmallow(app)

# Portfolio
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))

    def __init__(self, public_id, username, email, password):
        self.public_id = public_id
        self.username = username
        self.email = email
        self.password = password

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'public_id', 'username', 'email', 'password')

# Init schema
user_schema = UserSchema()


@app.route('/', methods=['GET'])
def index():
    # return jsonify({"about": "Hello, World!"})
    pass

@app.route('/new-user', methods=['GET'])
def get_new_user_form()
    pass

@app.route('/new-user', methods=['POST'])
def create_new_user():
    # data = request.get_json()

    # hashed_password = generate_password_hash(data['password'], method='sha256')

    # new_user = User(public_id=str(uuid4()), username=data['username'], email=data['email'], password=hashed_password)
    # db.session.add(new_user)
    # db.session.commit()

    # return jsonify({"user": new_user})
    pass

@app.route('/stocks/<string:ticker>', methods=['GET'])
def get_quote(ticker):
    # return jsonify({ticker: "results"})
    pass

@app.route('/watchlist/<string:ticker>', methods=['POST'])
def add_new_watched_item(ticker)
    pass

@app.route('/portfolio/<string:ticker>', methods=['GET'])
def get_new_position_form(ticker):
    pass

@app.route('/portfolio/<string:ticker>', methods=['POST'])
def add_new_position(ticker)
    data = request.get_json()

    pass

# Run Server
if __name__ == '__main__':
    app.run(debug=True)