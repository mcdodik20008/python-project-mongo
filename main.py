from fastapi import FastAPI
from pymongo import MongoClient

#https://github.com/mongodb-js/compass/releases
# fast-api-project / impotent-data
client = MongoClient('localhost', 27017)
mydb = client["fast-api-project"]
collection = mydb.get_collection("impotent-data")
for i in mydb.get_collection("impotent-data").find():
    print(i)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

