from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository import production_part as production_part_repository
from app.schemas import production_part as production_part_schema
from app.schemas.dto import production_part as production_part_dto

router = APIRouter(prefix="/production-parts", tags=["Production Parts"])

@router.post("/", response_model=production_part_schema.ProductionPart)
def create_production_part(production_part: production_part_dto.ProductionPartDTO, db: Session = Depends(get_db)):
    return production_part_repository.create_production_part(db, production_part)

@router.get(
    "/by-type/{part_type}", 
    response_model=list[production_part_schema.ProductionPartWithTimestamp]
)

def get_parts_by_type(
    part_type: str, 
    db: Session = Depends(get_db)
):
    rows = production_part_repository.get_parts_by_type_with_timestamp(db, part_type)
    if not rows:
        raise HTTPException(status_code=404, detail="No parts found for this type")
    return [
        {
            "id": _id,
            "part_id": part_id,
            "cycle_id": cycle_id,
            "stored_quantity": stored_qty,
            "part_type": p_type,
            "timestamp": ts,
        }
        for _id, part_id, cycle_id, stored_qty, p_type, ts in rows
    ]

@router.get("/get_utilization", response_model=int)
def get_utilization_part(db: Session = Depends(get_db)):
    return production_part_repository.get_utilization(db)

@router.get("/parts/{part_type}/total")
def get_total_quantity(
    part_type: str,
    db: Session = Depends(get_db)
):
    result = production_part_repository.get_total_quantity_by_part_type(db, part_type)
    if result["total_quantity"] == 0:
        raise HTTPException(status_code=404, detail="No parts found for this type")
    return result

@router.get("/summary")
def get_production_summary(db: Session = Depends(get_db)):
    return production_part_repository.get_production_summary(db)