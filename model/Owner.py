from pydantic import BaseModel, Field


class Owner(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    phone: str

