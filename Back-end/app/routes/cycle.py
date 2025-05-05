from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas import cycle as schemas
from app.repository import cycle as repository

router = APIRouter(prefix="/cycles", tags=["Cycles"])

@router.post("/", response_model=schemas.Cycle)
def create_cycle(cycle: schemas.CycleCreate, db: Session = Depends(get_db)):
    return repository.create_cycle(db=db, cycle=cycle)

@router.get("/", response_model=list[schemas.Cycle])
def get_all_cycles(db: Session = Depends(get_db)):
    return repository.get_all_cycles(db=db)

@router.get("/{cycle_id}", response_model=schemas.Cycle)
def get_cycle_by_id(cycle_id: int, db: Session = Depends(get_db)):
    db_cycle = repository.get_cycle_by_id(db=db, cycle_id=cycle_id)
    if db_cycle is None:
        raise HTTPException(status_code=404, detail="Cycle not found")
    return db_cycle
