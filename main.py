import json

from bson import json_util
from fastapi import FastAPI
from pymongo import MongoClient

#https://github.com/mongodb-js/compass/releases
# fast-api-project / impotent-data
client = MongoClient('localhost', 27017)
mydb = client["fast-api-project"]
collection = mydb.get_collection("impotent-data")


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/data-safety")
async def data_safety():
    for i in mydb.get_collection("impotent-data").find():
        return json.loads(json_util.dumps(i))