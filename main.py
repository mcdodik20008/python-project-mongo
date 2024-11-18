import os

from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId

# Инициализация приложения
app = FastAPI()

# Настройка шаблонов
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# Подключение к MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/vet_clinic")
client = AsyncIOMotorClient(MONGO_URI)
db = client["vet_clinic"]
animals_collection = db["animals"]
appointments_collection = db["appointments"]

# Модели данных
class Animal:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species

    def to_dict(self):
        return {"name": self.name, "age": self.age, "species": self.species}

# Маршруты для животных
@app.get("/")
async def read_animals(request: Request):
    animals = await animals_collection.find().to_list(100)
    return templates.TemplateResponse("animals.html", {"request": request, "animals": animals})

@app.get("/add-animal/")
async def add_animal_form(request: Request):
    return templates.TemplateResponse("add_animal.html", {"request": request})

@app.post("/add-animal/")
async def add_animal(name: str = Form(...), age: int = Form(...), species: str = Form(...)):
    animal = Animal(name, age, species)
    await animals_collection.insert_one(animal.to_dict())
    return RedirectResponse("/", status_code=302)


@app.post("/update-animal/{animal_id}")
async def update_animal(animal_id: str, request: Request):
    data = await request.json()
    if not ObjectId.is_valid(animal_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    result = await animals_collection.update_one(
        {"_id": ObjectId(animal_id)},
        {"$set": {
            "name": data["name"],
            "age": data["age"],
            "species": data["species"]
        }}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Animal not found")
    return RedirectResponse("/", status_code=302)

@app.delete("/delete-animal/{animal_id}")
async def delete_animal(animal_id: str):
    await animals_collection.delete_one({"_id": ObjectId(animal_id)})
    return RedirectResponse("/", status_code=302)
