from pydantic import BaseModel, Field

class Animal(BaseModel):
    id: str = Field(..., alias="_id") 
    name: str
    species: str
    age: int
    owner_id: str