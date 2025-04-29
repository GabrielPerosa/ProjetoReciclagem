from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository.cycle import create_cycle, get_cycles
from app.schemas.cycle import Cycle
from typing import List

router = APIRouter()

@router.post("/cycles/", response_model=Cycle)
def create_cycle_endpoint(cycle: Cycle, db: Session = Depends(get_db)):
    return create_cycle(db, cycle)

@router.get("/cycles/", response_model=List[Cycle])
def get_cycles_endpoint(db: Session = Depends(get_db)):
    return get_cycles(db)