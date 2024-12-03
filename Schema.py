from pydantic import BaseModel
from datetime import datetime

class AnimalCreate(BaseModel):
    name: str
    species: str
    age: int
    owner_id: str

class OwnerCreate(BaseModel):
    name: str
    phone: str

class DoctorCreate(BaseModel):
    name: str
    specialization: str

class AppointmentCreate(BaseModel):
    animal_id: str
    doctor_id: str
    appointment_time: datetime
    reason: str
