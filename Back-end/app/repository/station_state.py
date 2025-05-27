import uuid
from sqlalchemy.orm import Session
from app.models.station_state import StationStateDB
from app.schemas.dto.station_state import StationStateDTO
from datetime import datetime
from app.models.cycle import CycleDB
from app.models.station import StationDB

def create_station_state(db: Session, station_state_dto: StationStateDTO) -> StationStateDB:
    station = db.query(StationDB).filter(StationDB.id == station_state_dto.station_id).first()
    if not station:
        raise ValueError(f"Station with ID {station_state_dto.station_id} does not exist.")

    cycle = CycleDB(id=str(uuid.uuid4()))
    db.add(cycle)
    db.flush() 

    station_state = StationStateDB(
        id=str(uuid.uuid4()),
        station_id=station.id,   
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
