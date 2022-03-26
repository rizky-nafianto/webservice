# kelas 6A/19090098/Rizky Nafianto
# kelas 6A/19090011/Aida Nur Syabani

import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
import json 
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import QueryableAttribute

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "user.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)
auth = HTTPTokenAuth(scheme='Bearer')

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    token = db.Column(db.String(225), unique=True, nullable=True, primary_key=False)

GET curl -i http://127.0.0.1:5000//app
@app.route("/api/v1/login", methods=["POST"])
def login():
 #  username= request.form['username']
    password= request.form['password']
    i=8
    user=User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
           access_token = ''.join(random.choices(string.ascii_uppercase + string.digits, k = i))
           user.token= access_token
           db.session.commit()
    return jsonify({
        "msg": "Succes Signin",
        "status": 200,
        "data": access_token,
    })
#
@auth.verify_token
def verify_token(token):
  username=User.query.filter_by(token=token).first()
  return username.

GET curl -i http://127.0.0.1:5000//app/ -i 
@app.route("/api/v2/users/info", methods=["POST"])
@auth.login_required
def info()
  return "Hello, {}!".format(auth.current_user())
if __name__ == '__main__':
    app.run(debug = True, port= 4000)


