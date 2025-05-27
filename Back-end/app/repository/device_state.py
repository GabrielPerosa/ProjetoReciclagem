import uuid
from sqlalchemy.orm import Session
from app.models.device_state import DeviceStateDB
from app.schemas.dto.device_state import DeviceStateDTO

def create_device_state(db: Session, device_state_dto: DeviceStateDTO) -> DeviceStateDB:
    device_state = DeviceStateDB(
        id=str(uuid.uuid4()),
        device_id=device_state_dto.device_id,
        state=device_state_dto.state,
        timestamp=device_state_dto.timestamp,
    )
    db.add(device_state)
    db.commit()
    db.refresh(device_state)
    return device_state

def get_all_device_states(db: Session) -> list[DeviceStateDB]:
    return db.query(DeviceStateDB).all()
