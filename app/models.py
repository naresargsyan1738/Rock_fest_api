from sqlalchemy import Column, Integer, String
from app.database import Base


class RockGroup(Base):
    __tablename__ = "rock_groups"  

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
