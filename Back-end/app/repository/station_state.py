import uuid
from sqlalchemy.orm import Session
from app.models.station_state import StationStateDB
from app.schemas.dto.station_state import StationStateDTO
from datetime import datetime
from app.models.cycle import CycleDB

def create_station_state(db: Session, station_state_dto: StationStateDTO) -> StationStateDB:
    cycle = db.query(CycleDB).filter(CycleDB.id == station_state_dto.cycle_id).first()

    if not cycle:
        cycle = CycleDB(id=station_state_dto.cycle_id or str(uuid.uuid4()))
        db.add(cycle)
        db.flush()

    station_state = StationStateDB(
        id=str(uuid.uuid4()),
        station_id=station_state_dto.station_id,
        cycle_id=cycle.id,
        state=station_state_dto.state,
        timestamp=station_state_dto.timestamp or datetime.utcnow(),
    )
    db.add(station_state)
    db.commit()
    db.refresh(station_state)
    return station_state

def get_all_station_states(db: Session) -> list[StationStateDB]:
    return db.query(StationStateDB).all()
