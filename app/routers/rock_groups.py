from fastapi import APIRouter
from app.database import SessionLocal
from app import models
from app.schemas.rock_group import RockGroupCreate

router = APIRouter()


@router.get("/rock-groups")
def get_groups():
    db = SessionLocal()
    groups = db.query(models.RockGroup).all()
    db.close()
    return groups


@router.post("/rock-groups")
def add_group(group: RockGroupCreate):
    db = SessionLocal()
    new_group = models.RockGroup(name=group.name, country=group.country)
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    db.close()
    return new_group
