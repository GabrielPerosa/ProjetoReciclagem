from sqlalchemy.orm import Session
from app.models.sensor_state import SensorStateDB
from typing import List

def get_sensor_state(db: Session) -> List[SensorStateDB]:
    return db.query(SensorStateDB).all()

def create_sensor_state(db: Session, sensor_state_data: dict) -> SensorStateDB:
    db_sensor_state = SensorStateDB(**sensor_state_data)
    db.add(db_sensor_state)
    db.commit()
    db.refresh(db_sensor_state)
    return db_sensor_state
