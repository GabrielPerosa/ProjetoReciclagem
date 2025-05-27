import uuid
from sqlalchemy.orm import Session
from app.models.station import StationDB
from app.schemas.dto.station import StationDTO

def create_station(db: Session, station_dto: StationDTO) -> StationDB:
    station = StationDB(
        id=str(uuid.uuid4()),
        description=station_dto.description,
    )
    db.add(station)
    db.commit()
    db.refresh(station)
    return station

def get_all_stations(db: Session) -> list[StationDB]:
    return db.query(StationDB).all()
