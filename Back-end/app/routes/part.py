from fastapi import APIRouter, Depends
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
    return part_repository.get_all_parts(db)

@router.get("/quantity", response_model=int)
def get_quantity(db: Session = Depends(get_db)):
    return part_repository.get_quantity_parts(db)

@router.get("/type/{type}", response_model=Part)
def get_part_by_type(type: str, db: Session = Depends(get_db)):
    return part_repository.get_parts_by_type(db, type)

@router.get("/type/{type}/quantity", response_model=int)
def get_quantity_by_type(type: str, db: Session = Depends(get_db)):
    return part_repository.get_quantity_parts_by_type(db, type)
