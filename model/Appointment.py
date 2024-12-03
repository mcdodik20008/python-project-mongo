from datetime import datetime
from pydantic import BaseModel


class Appointment(BaseModel):
    animal_id: str  # Связь с животным
    doctor_id: str  # Связь с врачом
    appointment_time: datetime
    reason: str