from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository import station as station_repository
from app.schemas import station as station_schema
from app.schemas.dto import station as station_dto

router = APIRouter(prefix="/stations", tags=["Stations"])

@router.post("/", response_model=station_schema.Station)
def create_station(station: station_dto.StationDTO, db: Session = Depends(get_db)):
    return station_repository.create_station(db, station)

@router.get("/", response_model=list[station_schema.Station])
def get_all_stations(db: Session = Depends(get_db)):
    return station_repository.get_all_stations(db)
