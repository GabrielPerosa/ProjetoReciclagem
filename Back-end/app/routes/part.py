from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.part import Part
from app.schemas.dto.part import PartDTO
from app.repository import part as part_repository
from app.config.database import get_db

router = APIRouter(prefix="/parts", tags=["Parts"])

@router.post("/", response_model=Part)
def create_part(part: PartDTO, db: Session = Depends(get_db)):
    return part_repository.create_part(db, part)

@router.get("/", response_model=List[Part])
def list_all(db: Session = Depends(get_db)):
    parts = part_repository.list_all(db)
    return [{"id": p.id, "type": p.type, "quantity": q} for p, q in parts]

@router.get("/quantity/{type}", response_model=int)
def get_quantity(type: str, db: Session = Depends(get_db)):
    quantity = part_repository.get_quantity(db, type)
    if quantity is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return quantity