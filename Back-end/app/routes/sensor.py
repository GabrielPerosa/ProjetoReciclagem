from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.sensor import Sensor # Supondo que você tenha esses schemas
from app.repository.sensor import create_sensor, get_sensors  # Supondo que você tenha os métodos no repositório
from app.config.database import get_db
from typing import List

router = APIRouter(prefix="/sensors")

# Rota para listar sensores
@router.get("/", response_model=List[Sensor])
def list_sensors(db: Session = Depends(get_db)):
    return get_sensors(db)

# Rota para criar sensor
@router.post("/", response_model=Sensor)
def create_sensor_endpoint(sensor: Sensor, db: Session = Depends(get_db)):
    return create_sensor(db, sensor)