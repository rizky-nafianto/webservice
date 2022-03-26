import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
import secrets

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Content-Type'] = 'application/json'
    response.headers['Api-Name'] = 'Math-API'
    response.headers['Server'] = 'Poltek-Harber.io'
    response.headers['Request-ID'] = secrets.token_hex(32)
    return response

#curl -i -X GET http://127.0.0.1:7007/api/v1/square_with_parameters_in_url/2/3 -H 'Content-Type: application/json'
#curl -i -X GET http://127.0.0.1:7007/api/v1/square_with_parameters_in_url/2/3 # does it work?
@app.route("/api/v1/square_with_parameters_in_url/<a>/<b>", methods=["GET"])
def plus_with_parameters_in_url(a, b):
  return jsonify({"result": (int(a) ** int(b))}), 200

#curl -i -X POST http://127.0.0.1:7007/api/v1/square_with_parameters_not_in_url -d "a=2&b=3" -H 'Content-Type: application/json'
#curl -i -X POST http://127.0.0.1:7007/api/v1/square_with_parameters_not_in_url -d "a=2&b=3" # does it work?
@app.route("/api/v1/square_with_parameters_not_in_url", methods=["POST"])
def square_with_parameters_not_in_url():
  a = request.form.get("a")
  b = request.form.get("b")
  return jsonify({"result": (int(a) ** int(b))}), 200

#curl -i -X POST http://127.0.0.1:7007/api/v1/square_with_parameters_with_body_json -H 'Content-Type: application/json' -d '{"a":2, "b": 2}'
#curl -i -X POST http://127.0.0.1:7007/api/v1/square_with_parameters_with_body_json -d '{"a":2, "b": 2}' #does this work = ???
@app.route("/api/v1/square_with_parameters_with_body_json", methods=["POST"])
def square_with_parameters_with_body_json():
  a = request.json['a']
  b = request.json['b']
  return jsonify({"result": (int(a) ** int(b))}), 200

#curl -i -X POST http://127.0.0.1:7007/api/v1/square_with_parameters_in_header -H 'Content-Type: application/json' -H 'a: 2' -H 'b: 3'
@app.route("/api/v1/square_with_parameters_in_header", methods=["POST"])
def square_with_parameters_in_header():
  a = request.headers['a']
  b = request.headers['b']
  return jsonify({"result": (int(a) ** int(b))}), 200

if __name__ == '__main__':
   app.run(debug = True, port=7007)