from pydantic import BaseModel

class RockGroupCreate(BaseModel):
    name: str
    country: str
