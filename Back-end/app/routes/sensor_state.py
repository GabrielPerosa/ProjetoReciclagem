from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository.sensor_state import create_sensor_state, get_sensor_state
from app.schemas.sensor_state import SensorState
from typing import List

router = APIRouter(prefix="/sensor_state")

@router.post("/", response_model=SensorState)
def create_sensor_state_endpoint(sensor_state: SensorState, db: Session = Depends(get_db)):
    return create_sensor_state(db, sensor_state)

@router.get("/", response_model=List[SensorState])
def get_sensor_state_endpoint(db: Session = Depends(get_db)):
    return get_sensor_state(db)
