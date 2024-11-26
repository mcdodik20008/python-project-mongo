from pymongo import MongoClient
from faker import Faker
import random

client = MongoClient("mongodb://localhost:27017/")
db = client["animal_database"]

owners_collection = db["owners"]
vets_collection = db["vets"]
animals_collection = db["animals"]
appointments_collection = db["appointments"]

fake = Faker()

owners_collection.delete_many({})
vets_collection.delete_many({})
animals_collection.delete_many({})
appointments_collection.delete_many({})

def generate_owners(n=10):
    owners = []
    for _ in range(n):
        owners.append({
            "name": fake.name(),
            "contact_info": fake.phone_number(),
        })
    owners_collection.insert_many(owners)
    return list(owners_collection.find())

def generate_vets(n=5):
    vets = []
    for _ in range(n):
        vets.append({
            "name": fake.name(),
            "specialization": random.choice(["Therapy", "Surgery", "Dentistry"]),
        })
    vets_collection.insert_many(vets)
    return list(vets_collection.find())

def generate_animals(owners, n=20):
    """Создает n животных."""
    animals = []
    for _ in range(n):
        owner = random.choice(owners)
        animals.append({
            "name": fake.first_name(),
            "age": random.randint(1, 15),
            "species": random.choice(["Cat", "Dog", "Parrot"]),
            "owner_id": owner["_id"],
        })
    animals_collection.insert_many(animals)
    return list(animals_collection.find())

def generate_appointments(animals, vets, n=15):
    appointments = []
    for _ in range(n):
        animal = random.choice(animals)  # Выбираем случайное животное
        vet = random.choice(vets)  # Выбираем случайного ветеринара
        appointments.append({
            "date": fake.date_time_between(start_date="-1y", end_date="now").isoformat(),
            "reason": random.choice(["Routine check-up", "Vaccination", "Illness"]),
            "animal_id": animal["_id"],  # Ссылка на животное
            "vet_id": vet["_id"],  # Ссылка на ветеринара
        })
    appointments_collection.insert_many(appointments)
    return list(appointments_collection.find())

try:
    print("Генерация данных...")

    owners = generate_owners(10)
    print(f"Создано владельцев: {len(owners)}")

    vets = generate_vets(5)
    print(f"Создано ветеринаров: {len(vets)}")

    animals = generate_animals(owners, 20)
    print(f"Создано животных: {len(animals)}")

    appointments = generate_appointments(animals, vets, 15)
    print(f"Создано записей на прием: {len(appointments)}")

    print("Миграция завершена.")
finally:
    client.close()
