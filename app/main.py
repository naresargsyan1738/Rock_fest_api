from fastapi import FastAPI
from app.routers import rock_groups

app = FastAPI()

app.include_router(rock_groups.router)
