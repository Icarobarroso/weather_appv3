import requests
from pymongo import MongoClient
import os
from Config.vars import API_KEY


def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def save_to_mongodb(data):
    client = MongoClient(os.environ["MONGO_URI"])
    db = client["weather_db"]
    collection = db["forecast"]
    collection.insert_one(data)

if __name__ == "__main__":
    city = "new york"
    weather_data = fetch_weather_data(city)
    save_to_mongodb(weather_data)