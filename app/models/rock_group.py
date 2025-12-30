from sqlalchemy import Column, Integer, String, JSON
from app.database import Base


class RockGroup(Base):
    tablename = "rock_groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    foundation_year = Column(Integer, nullable=False)
    producer = Column(String, nullable=True)
    genre = Column(String, nullable=False)

    members = Column(JSON, nullable=True)
