from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository.part import create_part, get_parts
from app.schemas.part import Part
from typing import List

router = APIRouter(prefix="/parts")

@router.post("/", response_model=Part)
def create_part_endpoint(part: Part, db: Session = Depends(get_db)):
    return create_part(db, part)

@router.get("/", response_model=List[Part])
def get_parts_endpoint(db: Session = Depends(get_db)):
    return get_parts(db)
