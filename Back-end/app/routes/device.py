from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository import device as device_repository
from app.schemas import device as device_schema
from app.schemas.dto import device as device_dto

router = APIRouter(prefix="/devices", tags=["Devices"])

@router.post("/", response_model=device_schema.Device)
def create_device(device: device_dto.DeviceDTO, db: Session = Depends(get_db)):
    return device_repository.create_device(db, device)

@router.get("/", response_model=list[device_schema.Device])
def get_all_devices(db: Session = Depends(get_db)):
    return device_repository.get_all_devices(db)
