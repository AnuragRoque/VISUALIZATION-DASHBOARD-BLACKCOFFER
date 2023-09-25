from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


app = Flask(__name__)
CORS(app)
uri = "mongodb+srv://anuragsingh2445:xJJjhIt4zM28DvZ2@cluster0.hvmrxdi.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))  # Replace with your MongoDB connection string
db = client["VISUALIZATION-DASHBOARD-BLACKCOFFER"]  # Replace with your database name
collection = db["c2"]  # Replace with your collection name

@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))  # Exclude the '_id' field
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)



