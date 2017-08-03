import os
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

client = MongoClient(
    'database',
    27017)
db = client.tripsdb



@app.route('/auth', methods=['GET'])
def testAction():
    if 'X-Consumer-Custom-ID' in request.headers:
        userId = request.headers['X-Consumer-Custom-ID']
        user = db.tripsdb.find_one({'_id': ObjectId(userId)})
        user['_id'] = userId
        user = jsonify(user)
    else:
        user = 'no user'
    return user


@app.route('/user', methods=['POST'])
def addUser():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['surname'],
        'email': request.form['email'],
        'image': request.form['image']

    }
    inserted = db.tripsdb.insert_one(item_doc)
    return jsonify(str(inserted.inserted_id))

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    if 'X-Consumer-Custom-ID' in request.headers:
        if request.headers['X-Consumer-Custom-ID'] == id:
            user = db.tripsdb.find_one({'_id': ObjectId(id)})
            user['_id'] = id
            return jsonify(user)
        else:
            return "you cannot see others people info!"
    else:
        return "not logged in"





@app.route('/user/<id>/trips', methods=['POST'])
def addTripAction(id):
    data = request.get_json()
    user = db.tripsdb.find_one({'_id': ObjectId(id)})
    if 'trips' in user:
        trips = user['trips'] + [data]
    else:
        trips = [data]

    db.tripsdb.update({'_id': ObjectId(id)}, {'$set': {'trips': trips}})

    return jsonify({"status": "ok", "data": user['name']})

@app.route('/user/<id>/trips', methods=['GET'])
def getTripAction(id):
    user = db.tripsdb.find_one({'_id': ObjectId(id)})
    if 'trips' in user:
        trips = user['trips']
    else:
        trips = []
    return jsonify({"status": "ok", "trips": trips})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
