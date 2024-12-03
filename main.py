from fastapi import FastAPI
from fastapi import HTTPException
from typing import List
from datetime import datetime
from bson.objectid import ObjectId
from model.Animal import Animal
from model.Owner import Owner
from model.Vet import Vet
from model.Appointment import Appointment
from Schema import AnimalCreate, OwnerCreate, DoctorCreate, AppointmentCreate
import db

app = FastAPI()

@app.post("/animals/", response_model=Animal)
async def create_animal(animal: AnimalCreate):
    if isinstance(animal.owner_id, ObjectId):
        animal.owner_id = str(animal.owner_id)

    animal_data = animal.dict()
    result = db.animals.insert_one(animal_data)

    animal_data["_id"] = str(result.inserted_id)

    return animal_data


@app.get("/animals/", response_model=List[Animal])
async def get_animals():
    animals = list(db.animals.find())
    
    for animal in animals:
        if "_id" in animal:
            animal["_id"] = str(animal["_id"])
        if "owner_id" in animal and isinstance(animal["owner_id"], ObjectId):
            animal["owner_id"] = str(animal["owner_id"])
    
    return animals

# Создание владельца
@app.post("/owners/", response_model=Owner)
async def create_owner(owner: OwnerCreate):
    owner_data = owner.dict()

    result = db.owners.insert_one(owner_data)
    owner_data["_id"] = str(result.inserted_id)

    return owner_data

# Получение всех владельцев
@app.get("/owners/", response_model=List[Owner])
async def get_owners():
    owners = list(db.owners.find())

    for owner in owners:
        if "_id" in owner:
            owner["_id"] = str(owner["_id"])

    return owners

# Создание ветеринара
@app.post("/doctors/", response_model=Vet)
async def create_doctor(doctor: DoctorCreate):
    doctor_data = doctor.dict()

    result = db.doctors.insert_one(doctor_data)
    doctor_data["_id"] = str(result.inserted_id)

    return doctor_data

# Получение всех ветеринаров
@app.get("/doctors/", response_model=List[Vet])
async def get_doctors():
    doctors = list(db.doctors.find())

    for doctor in doctors:
        if "_id" in doctor:
            doctor["_id"] = str(doctor["_id"])

    return doctors

# Создание записи на приём
@app.post("/appointments/", response_model=Appointment)
async def create_appointment(appointment: AppointmentCreate):
    appointment_data = appointment.dict()

    appointment_data["appointment_time"] = appointment.appointment_time.isoformat()
    result = db.appointments.insert_one(appointment_data)
    appointment_data["_id"] = str(result.inserted_id)

    return appointment_data

# Получение всех записей на приём
@app.get("/appointments/", response_model=List[Appointment])
async def get_appointments():
    appointments = list(db.appointments.find())

    for appointment in appointments:
        if "_id" in appointment:
            appointment["_id"] = str(appointment["_id"])
        if "appointment_time" in appointment:
            appointment["appointment_time"] = datetime.fromisoformat(appointment["appointment_time"])

    return appointments

# Получение записи на приём по ID
@app.get("/appointments/{appointment_id}/", response_model=Appointment)
async def get_appointment(appointment_id: str):
    try:
        appointment = db.appointments.find_one({"_id": ObjectId(appointment_id)})
        if appointment is None:
            raise HTTPException(status_code=404, detail="Запись на приём не найдена")
        appointment["_id"] = str(appointment["_id"])
        if "appointment_time" in appointment:
            appointment["appointment_time"] = datetime.fromisoformat(appointment["appointment_time"])
        return appointment
    except Exception:
        raise HTTPException(status_code=400, detail="Неверный формат ID")
