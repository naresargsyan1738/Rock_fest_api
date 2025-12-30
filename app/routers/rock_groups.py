from fastapi import APIRouter

router = APIRouter()


@router.get("/rock-groups")
def get_rock_groups():
    return {"message": "Rock groups API works!"}
