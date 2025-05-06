from sqlalchemy.orm import Session
from app.models.workstation_state import WorkstationStateDB
from app.schemas.dto.workstation_state import WorkstationStateDTO
from app.schemas.workstation_state import WorkstationState

def create_workstation_state(db: Session, state_dto: WorkstationStateDTO) -> WorkstationState:
    state = WorkstationStateDB(
        status=state_dto.state,
        timestamp=state_dto.timestamp,
        workstation_id=state_dto.workstation_id
    )
    db.add(state)
    db.commit()
    db.refresh(state)
    return state

def get_all_workstation_states(db: Session) -> list[WorkstationState]:
    return db.query(WorkstationStateDB).all()
