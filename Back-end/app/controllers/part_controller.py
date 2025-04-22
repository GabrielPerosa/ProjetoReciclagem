from fastapi import APIRouter
from models.part_model import Part

router = APIRouter(prefix="/parts")
parts_db = []

@router.get("/")
def list_parts():
    return parts_db

@router.post("/")
def create_parts(data: Part):
    parts_db.append(data)
    return {"message": "Created successfully"}
