from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class RockGroup(Base):
    __tablename__ = "rock_groups"  

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    foundation_year = Column(Integer, nullable=True)  
    members = Column(JSON, nullable=True)  

    albums = relationship("Album", back_populates="group")  

class Album(Base):
    __tablename__ = "albums" 

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("rock_groups.id"))

    group = relationship("RockGroup", back_populates="albums")
