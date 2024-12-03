from pydantic import BaseModel, Field

class Vet(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    specialization: str