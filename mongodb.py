import requests
import pymongo
from pymongo import MongoClient
import time

# MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["sensor_data"]  # Database name
collection = db["readings"]  # Collection name

DEVICE_ID = "test"
TOKEN = "YOUR_UBIDOTS_TOKEN"
url = f"http://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_ID}/variables/"

while True:
    # Fetch data from Ubidots
    response = requests.get(url, headers={"X-Auth-Token": TOKEN})
    if response.status_code == 200:
        data = response.json()
        motion_detected = next(var for var in data['results'] if var['name'] == 'motion_detected')
        ldr_value = next(var for var in data['results'] if var['name'] == 'ldr_value')
        temperature = next(var for var in data['results'] if var['name'] == 'temperature')
        humidity = next(var for var in data['results'] if var['name'] == 'humidity')

        # Store the data in MongoDB
        collection.insert_one({
            "motion_detected": motion_detected['last_value'],
            "ldr_value": ldr_value['last_value'],
            "temperature": temperature['last_value'],
            "humidity": humidity['last_value'],
            "timestamp": time.time()
        })
        print("Data saved to MongoDB.")

    time.sleep(60)  # Delay before next data pull