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
@router.get("/rock-groups/{group_id}")
def get_group(group_id: int):
    db = SessionLocal()
    group = db.query(models.RockGroup).filter(models.RockGroup.id == group_id).first()
    db.close()
    return group

@router.delete("/rock-groups/{group_id}")
def delete_group(group_id: int):
    db = SessionLocal()
    group = db.query(models.RockGroup).filter(models.RockGroup.id == group_id).first()

    if group:
        db.delete(group)
        db.commit()
        db.close()
        return {"status": "deleted"}

    db.close()
    return {"status": "not found"}
@router.put("/rock-groups/{group_id}")
def update_group(group_id: int, new_data: RockGroupCreate):
    db = SessionLocal()
    group = db.query(models.RockGroup).filter(models.RockGroup.id == group_id).first()

    if group:
        group.name = new_data.name
        group.country = new_data.country
        db.commit()
        db.refresh(group)
        db.close()
        return group

    db.close()
    return {"status": "not found"}
