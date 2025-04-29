from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.workstation_state import WorkstationState
from app.config.database import get_db
from app.repository.workstation_state import create_workstation_state, get_workstation_states
from typing import List

router = APIRouter(prefix="/workstation_states")

@router.post("/", response_model=WorkstationState)
def create_workstation_state_endpoint(state: WorkstationState, db: Session = Depends(get_db)):
    return create_workstation_state(db, state)

@router.get("/", response_model=List[WorkstationState])
def list_workstation_states(db: Session = Depends(get_db)):
    return get_workstation_states(db)
