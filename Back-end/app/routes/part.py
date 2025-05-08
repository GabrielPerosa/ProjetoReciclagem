from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.part import Part
from app.schemas.dto.part import PartDTO
from app.repository import part as part_repository
from app.config.database import get_db

router = APIRouter(prefix="/parts", tags=["Parts"])

@router.post("/", response_model=Part)
def create(part_dto: PartDTO, db: Session = Depends(get_db)):
    return part_repository.create_part(db, part_dto)

@router.get("/", response_model=list[Part])
def list_all(db: Session = Depends(get_db)):
    return part_repository.get_all_parts(db)
