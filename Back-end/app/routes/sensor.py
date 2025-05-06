from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.sensor import Sensor
from app.schemas.dto.sensor import SensorDTO
from app.repository import sensor as sensor_repository
from app.config.database import get_db

router = APIRouter(prefix="/sensors", tags=["Sensors"])

@router.post("/", response_model=Sensor)
def create(sensor_dto: SensorDTO, db: Session = Depends(get_db)):
    return sensor_repository.create_sensor(db, sensor_dto)

@router.get("/", response_model=list[Sensor])
def list_all(db: Session = Depends(get_db)):
    return sensor_repository.get_all_sensors(db)
