import uuid
from sqlalchemy.orm import Session
from app.models.sensor_state import SensorStateDB
from app.schemas.dto.sensor_state import SensorStateDTO
from app.schemas.sensor_state import SensorState

def create_sensor_state(db: Session, sensor_state_dto: SensorStateDTO) -> SensorState:
    sensor_state = SensorStateDB(
        id=str(uuid.uuid4()),
        state=sensor_state_dto.state,
        timestamp=sensor_state_dto.timestamp,
        sensor_id=sensor_state_dto.sensor_id
    )
    db.add(sensor_state)
    db.commit()
    db.refresh(sensor_state)
    return sensor_state

def get_all_sensor_states(db: Session) -> list[SensorState]:
    return db.query(SensorStateDB).all()