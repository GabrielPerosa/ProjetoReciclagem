from sqlalchemy.orm import Session
from app.models.sensor import SensorDB
from app.schemas.dto.sensor import SensorDTO
from app.schemas.sensor import Sensor

def create_sensor(db: Session, sensor_dto: SensorDTO) -> Sensor:
    sensor = SensorDB(description=sensor_dto.description)
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor

def get_all_sensors(db: Session) -> list[Sensor]:
    return db.query(SensorDB).all()