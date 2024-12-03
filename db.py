from pymongo import MongoClient
from typing import Any

# Создание подключения к базе данных
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["vet_clinic"]

animals = db["animals"]
owners = db["owners"]
doctors = db["doctors"]
appointments = db["appointments"]
