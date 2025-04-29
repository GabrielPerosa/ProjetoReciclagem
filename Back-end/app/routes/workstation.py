from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.workstation import Workstation
from app.repository.workstation import create_workstation, get_workstations
from app.config.database import get_db
from typing import List

router = APIRouter(prefix="/workstations")

@router.get("/", response_model=List[Workstation])
def list_workstations(db: Session = Depends(get_db)):
    return get_workstations(db)

@router.post("/", response_model=Workstation)
def create_workstation_endpoint(workstation: Workstation, db: Session = Depends(get_db)):
    return create_workstation(db, workstation)
