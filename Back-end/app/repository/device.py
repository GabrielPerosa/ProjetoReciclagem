import uuid
from sqlalchemy.orm import Session
from app.models.device import DeviceDB
from app.schemas.dto.device import DeviceDTO

def create_device(db: Session, device_dto: DeviceDTO) -> DeviceDB:
    device = DeviceDB(
        id=str(uuid.uuid4()),
        description=device_dto.description,
    )
    db.add(device)
    db.commit()
    db.refresh(device)
    return device

def get_all_devices(db: Session) -> list[DeviceDB]:
    return db.query(DeviceDB).all()
