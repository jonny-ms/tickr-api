from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Init app
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"about": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)