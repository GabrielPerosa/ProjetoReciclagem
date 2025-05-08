from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.cycle import Cycle
from app.schemas.dto.cycle import CycleDTO
from app.repository import cycle as cycle_repository
from app.config.database import get_db

router = APIRouter(prefix="/cycles", tags=["Cycles"])

@router.post("/", response_model=Cycle)
def create(cycle_dto: CycleDTO, db: Session = Depends(get_db)):
    return cycle_repository.create_cycle(db, cycle_dto)

@router.get("/", response_model=list[Cycle])
def list_all(db: Session = Depends(get_db)):
    return cycle_repository.get_all_cycles(db)
