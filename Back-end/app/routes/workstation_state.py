from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.workstation_state import WorkstationState
from app.schemas.dto.workstation_state import WorkstationStateDTO
from app.repository import workstation_state as ws_state_repository
from app.config.database import get_db

router = APIRouter(prefix="/workstation_states", tags=["Workstation States"])

@router.post("/", response_model=WorkstationState)
def create(state_dto: WorkstationStateDTO, db: Session = Depends(get_db)):
    return ws_state_repository.create_workstation_state(db, state_dto)

@router.get("/", response_model=list[WorkstationState])
def list_all(db: Session = Depends(get_db)):
    return ws_state_repository.get_all_workstation_states(db)
