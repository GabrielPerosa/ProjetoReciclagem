from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository import station_state as station_state_repository
from app.schemas import station_state as station_state_schema
from app.schemas.dto import station_state as station_state_dto

router = APIRouter(prefix="/station-states", tags=["Station States"])

@router.post("/", response_model=station_state_schema.StationState)
def create_station_state(station_state: station_state_dto.StationStateDTO, db: Session = Depends(get_db)):
    return station_state_repository.create_station_state(db, station_state)

@router.get("/", response_model=list[station_state_schema.StationState])
def get_all_station_states(db: Session = Depends(get_db)):
    return station_state_repository.get_all_station_states(db)
