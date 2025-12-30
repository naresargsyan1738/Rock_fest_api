from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import rock_groups

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(rock_groups.router)
