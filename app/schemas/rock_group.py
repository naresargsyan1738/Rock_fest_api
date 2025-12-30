from pydantic import BaseModel


class RockGroup(BaseModel):
    name: str
    foundation_year: int
    genre: str
