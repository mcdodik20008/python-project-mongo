from pymongo.collection import Collection
from model import Owner, Animal, Vet, Appointment
from bson import ObjectId
from db import get_collection

def create_owner(owner_data: dict) -> dict:
    owners_collection = get_collection("owners")
    owner = Owner(**owner_data)
    owners_collection.insert_one(owner.to_dict())
    return owner.to_dict()


def get_owners() -> list:
    owners_collection = get_collection("owners")
    return list(owners_collection.find())


def get_owner(owner_id: str) -> dict:
    owners_collection = get_collection("owners")
    owner = owners_collection.find_one({"_id": ObjectId(owner_id)})
    if not owner:
        return None
    return owner


def create_animal(animal_data: dict) -> dict:
    animals_collection = get_collection("animals")
    animal = Animal(**animal_data)
    animals_collection.insert_one(animal.to_dict())
    return animal.to_dict()


def get_animals() -> list:
    animals_collection = get_collection("animals")
    return list(animals_collection.find())


def get_animal(animal_id: str) -> dict:
    animals_collection = get_collection("animals")
    animal = animals_collection.find_one({"_id": ObjectId(animal_id)})
    if not animal:
        return None
    return animal


def create_vet(vet_data: dict) -> dict:
    vets_collection = get_collection("vets")
    vet = Vet(**vet_data)
    vets_collection.insert_one(vet.to_dict())
    return vet.to_dict()


def create_appointment(appointment_data: dict) -> dict:
    appointments_collection = get_collection("appointments")
    appointment = Appointment(**appointment_data)
    appointments_collection.insert_one(appointment.to_dict())
    return appointment.to_dict()
