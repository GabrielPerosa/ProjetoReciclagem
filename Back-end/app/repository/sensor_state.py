from sqlalchemy.orm import Session
from app.models.sensor_state import SensorStateDB
from typing import List

# Função para obter todos os estados dos sensores
def get_sensor_state(db: Session) -> List[SensorStateDB]:
    return db.query(SensorStateDB).all()

# Função para criar um novo estado de sensor
def create_sensor_state(db: Session, sensor_state_data: dict) -> SensorStateDB:
    db_sensor_state = SensorStateDB(**sensor_state_data)
    db.add(db_sensor_state)
    db.commit()
    db.refresh(db_sensor_state)
    return db_sensor_state
