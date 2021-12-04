from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
import login_signup

# importing necessary packages

app = Flask(__name__)
CORS(app)
api = Api(app)
CORS(app, support_credentials=True)


# SignUP section
@app.route('/api/v1/new_data', methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def post():
    if (request.method == 'POST'):
        args = request.get_json()
        result = login_signup.signUp(args['username'], args['password'], args['name'], args['email'])
        print(result)
        if result != False:
            jsonData = jsonify(result)
            return jsonData
        else:
            return {"success": "false"}

# Login section
@app.route('/api/v1/check', methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def post_login():
    if (request.method == 'POST'):
        print("test0")
        args = request.get_json()
        result = login_signup.login(args['username'], args['password'])
        print("test")
        print(result)
        # login_signup.login(args['username'], args['password'])
        if result != False:
            jsonData = jsonify(result)
            return jsonData
        else:
            return {"success": "false"}


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
