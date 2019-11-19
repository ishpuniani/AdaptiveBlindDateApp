from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask import Flask, jsonify, request, make_response
from pymongo import MongoClient
from functools import wraps
import uuid
import datetime
import jwt
from flask_cors import CORS

#import services here
from services.match_recommender import MatchRecommender

#-----------------------------------------------------------------------------------------------------------------
#                                     App Initialization
#-----------------------------------------------------------------------------------------------------------------
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'thisissecret'

#-----------------------------------------------------------------------------------------------------------------
#                                     DB Configuration
#-----------------------------------------------------------------------------------------------------------------
client = MongoClient("mongodb+srv://niobrara:niobrara123@adaptiveblinddateapp-hdqaj.mongodb.net/test")
db = client.timble

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = db.user.find_one({'public_id':data['public_id']})
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

#-----------------------------------------------------------------------------------------------------------------
#                                     Default Routes
#-----------------------------------------------------------------------------------------------------------------
@app.route('/')
@app.route('/health/iamalive')
def index():
    return "Hello, World!"

#-----------------------------------------------------------------------------------------------------------------
#                                     Login and SignUp
#-----------------------------------------------------------------------------------------------------------------
@app.route('/signup', methods=['POST'])
def add_user():
    _json = request.get_json()
    _name = _json['name']
    _email = _json['email']
    _mobile = _json['mobile']
    _password = _json['password']
    _public_id = str(uuid.uuid4())
    
    # validate the received values
    if _name and _email and _mobile and _password and request.method == 'POST':

        #check email exists
        user = db.user.find_one({'email': _email})

        if user:
            resp = jsonify('Email already exists. Sign in instead.')
            resp.status_code = 500
            return resp
        
        # do not save password as a plain text
        _hashed_password = generate_password_hash(_password)
        # save details
        db.user.insert({'public_id': _public_id,'name': _name, 'email': _email, 'mobile': _mobile, 'password': _hashed_password})
        resp = jsonify('User added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/login', methods=['POST'])
def login():
    _json = request.get_json()
    _email = _json['email']
    _password = _json['password']
    user = db.user.find_one({'email': _email})

    if not user:
        return unauthorized()

    if check_password_hash(user['password'], _password):
        token = jwt.encode({'public_id' : user['public_id'],'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=15)},app.config['SECRET_KEY']) 

        return jsonify({'token' : token.decode('UTF-8')})

    return unauthorized()


#-----------------------------------------------------------------------------------------------------------------
#                                     User related APIs
#-----------------------------------------------------------------------------------------------------------------
@app.route('/users')
# @token_required
def users():
    users = db.user.find()
    users = dumps(users)

    return jsonify({'users' : users})


@app.route('/user/<id>')
def user(id):
    user = db.user.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp


@app.route('/update', methods=['PUT'])
def update_user():
    _json = request.get_json()
    _id = _json['_id']
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']
    # validate the received values
    if _name and _email and _password and _id and request.method == 'PUT':
        # do not save password as a plain text
        _hashed_password = generate_password_hash(_password)
        # save edits
        db.user.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(
            _id)}, {'$set': {'name': _name, 'email': _email, 'password': _hashed_password}})
        resp = jsonify('User updated successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()


@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    db.user.delete_one({'_id': ObjectId(id)})
    resp = jsonify('User deleted successfully!')
    resp.status_code = 200
    return resp


#-----------------------------------------------------------------------------------------------------------------
#                                     Error Handlers
#-----------------------------------------------------------------------------------------------------------------
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.errorhandler(401)
def unauthorized(error=None):
    message = {
        'status': 401,
        'message': 'Unathorized Access!!'
    }
    resp = jsonify(message)
    resp.status_code = 401

    return resp

@app.errorhandler(500)
def internal_server_error(error=None):
    message = {
        'status': 500,
        'message': 'Something went wrong!'
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp

#-----------------------------------------------------------------------------------------------------------------
#                                     Recommendation Engine
#-----------------------------------------------------------------------------------------------------------------
@app.route('/recommend/<public_id>', methods=['GET'])
def get_recommendations(public_id):
    try:
        mr = MatchRecommender(db)
        resp = mr.get_recommended_matches(public_id)
        return resp
    except:
        return internal_server_error()

if __name__ == "__main__":
    app.run()
