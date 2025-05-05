from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas import part as schemas
from app.repository import part as repository

router = APIRouter(prefix="/parts", tags=["Parts"])

@router.post("/", response_model=schemas.Part)
def create_part(part: schemas.PartCreate, db: Session = Depends(get_db)):
    return repository.create_part(db=db, part=part)

@router.get("/", response_model=list[schemas.Part])
def get_all_parts(db: Session = Depends(get_db)):
    return repository.get_all_parts(db=db)

@router.get("/{part_id}", response_model=schemas.Part)
def get_part_by_id(part_id: int, db: Session = Depends(get_db)):
    db_part = repository.get_part_by_id(db=db, part_id=part_id)
    if db_part is None:
        raise HTTPException(status_code=404, detail="Part not found")
    return db_part
