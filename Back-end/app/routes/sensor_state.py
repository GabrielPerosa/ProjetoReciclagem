from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.sensor_state import SensorState
from app.schemas.dto.sensor_state import SensorStateDTO
from app.repository import sensor_state as sensor_state_repository
from app.config.database import get_db

router = APIRouter(prefix="/sensor_states", tags=["Sensor States"])

@router.post("/", response_model=SensorState)
def create(sensor_state_dto: SensorStateDTO, db: Session = Depends(get_db)):
    return sensor_state_repository.create_sensor_state(db, sensor_state_dto)

@router.get("/", response_model=list[SensorState])
def list_all(db: Session = Depends(get_db)):
    return sensor_state_repository.get_all_sensor_states(db)
