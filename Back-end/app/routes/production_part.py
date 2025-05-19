from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository import production_part as production_part_repository
from app.schemas import production_part as production_part_schema
from app.schemas.dto import production_part as production_part_dto

router = APIRouter(prefix="/production-parts", tags=["Production Parts"])

@router.post("/", response_model=production_part_schema.ProductionPart)
def create_production_part(production_part: production_part_dto.ProductionPartDTO, db: Session = Depends(get_db)):
    return production_part_repository.create_production_part(db, production_part)

@router.get("/", response_model=list[production_part_schema.ProductionPart])
def get_all_production_parts(db: Session = Depends(get_db)):
    return production_part_repository.get_all_production_parts(db)
