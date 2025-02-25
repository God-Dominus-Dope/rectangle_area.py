from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["sensor_data"]
collection = db["readings"]

# Modified index route to return JSON
@app.route('/')
def index():
    message = {"status": "API is working", "message": "Welcome to the Sensor Data API"}
    return jsonify(message)

@app.route('/api/sensor_data', methods=['GET'])
def get_sensor_data():
    # Fetch the latest sensor readings
    sensor_data = collection.find().sort([('_id', -1)]).limit(10)  # Get the last 10 readings
    data = []
    for reading in sensor_data:
        data.append({
            "motion_detected": reading['motion_detected'],
            "ldr_value": reading['ldr_value'],
            "temperature": reading['temperature'],
            "humidity": reading['humidity'],
            "timestamp": reading['timestamp']
        })
    return jsonify(data)

if _name_ == '__main__':
    app.run(debug=True)