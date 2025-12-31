from sqlalchemy import func
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
@router.get("/rock-groups/search")
def search_groups(country: str):
    db = SessionLocal()
    groups = db.query(models.RockGroup).filter(models.RockGroup.country == country).all()
    db.close()
    return groups

@router.get("/rock-groups/{group_id}/albums")
def get_group_albums(group_id: int):
    db = SessionLocal()
    data = db.query(models.Album).filter(models.Album.group_id == group_id).all()
    db.close()
    return data

@router.get("/rock-groups/filter")
def filter_groups(country: str, year: int):
    db = SessionLocal()
    data = db.query(models.RockGroup).filter(
        models.RockGroup.country == country,
        models.RockGroup.foundation_year >= year
    ).all()
    db.close()
    return data

@router.put("/rock-groups/{group_id}/rename")
def rename_group(group_id: int, new_name: str):
    db = SessionLocal()
    group = db.query(models.RockGroup).filter(models.RockGroup.id == group_id).first()
    if not group:
        return {"error": "Group not found"}

    group.name = new_name
    db.commit()
    db.refresh(group)
    db.close()
    return {"message": "updated", "group": group.name}


@router.get("/stats/countries")
def stats_by_country():
    db = SessionLocal()
    data = db.query(
        models.RockGroup.country,
        func.count(models.RockGroup.id)
    ).group_by(models.RockGroup.country).all()
    db.close()
    return data

@router.get("/rock-groups/sort")
def sort_groups(order: str = "asc"):
    db = SessionLocal()
    if order == "desc":
        result = db.query(models.RockGroup).order_by(models.RockGroup.name.desc()).all()
    else:
        result = db.query(models.RockGroup).order_by(models.RockGroup.name.asc()).all()
    db.close()
    return result

@router.get("/rock-groups/page")
def get_groups_page(page: int = 1, limit: int = 5):
    db = SessionLocal()
    offset = (page - 1) * limit
    groups = db.query(models.RockGroup).offset(offset).limit(limit).all()
    db.close()
    return groups
