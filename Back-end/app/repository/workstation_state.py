from sqlalchemy.orm import Session
from app.models.workstation_state import WorkstationState as WorkstationStateModel
from app.schemas.workstation_state import WorkstationState 

def create_workstation_state(db: Session, state: WorkstationState):
    db_state = WorkstationStateModel(
        state=state.state,
        timestamp=state.timestamp,
        workstation_id=state.workstation_id
    )
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state

def get_workstation_states(db: Session):
    return db.query(WorkstationStateModel).all()
