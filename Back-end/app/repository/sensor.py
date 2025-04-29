from sqlalchemy.orm import Session
from app.models.sensor import SensorDB
from app.schemas.sensor import Sensor

# Função para criar um sensor no banco
def create_sensor(db: Session, sensor: Sensor):
    db_sensor = SensorDB(description=sensor.description)
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

# Função para listar todos os sensores
def get_sensors(db: Session):
    return db.query(SensorDB).all()