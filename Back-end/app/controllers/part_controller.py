from fastapi import APIRouter
from models.part_model import Part

router = APIRouter(prefix="/parts")
parts_db = []

@router.get("/")
def list_parts():
    return parts_db

@router.post("/update/{part_id}")
def update_peca(part_id: int, data: Part):
    for i, part in enumerate(parts_db):
        if part.id == part_id:
            parts_db[i] = data
            return {"message": "Updated part"}
    return {"message": "Part not found"}
