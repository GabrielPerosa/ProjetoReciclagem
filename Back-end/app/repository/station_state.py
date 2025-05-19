import uuid
from sqlalchemy.orm import Session
from app.models.station_state import StationStateDB
from app.schemas.dto.station_state import StationStateDTO

def create_station_state(db: Session, station_state_dto: StationStateDTO) -> StationStateDB:
    station_state = StationStateDB(
        id=str(uuid.uuid4()),
        station_id=station_state_dto.station_id,
        cycle_id=station_state_dto.cycle_id,
        state=station_state_dto.state,
        timestamp=station_state_dto.timestamp,
    )
    db.add(station_state)
    db.commit()
    db.refresh(station_state)
    return station_state

def get_all_station_states(db: Session) -> list[StationStateDB]:
    return db.query(StationStateDB).all()
