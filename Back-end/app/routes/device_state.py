from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository import device_state as device_state_repository
from app.schemas import device_state as device_state_schema
from app.schemas.dto import device_state as device_state_dto

router = APIRouter(prefix="/device-states", tags=["Device States"])

@router.post("/", response_model=device_state_schema.DeviceState)
def create_device_state(device_state: device_state_dto.DeviceStateDTO, db: Session = Depends(get_db)):
    return device_state_repository.create_device_state(db, device_state)

@router.get("/", response_model=list[device_state_schema.DeviceState])
def get_all_device_states(db: Session = Depends(get_db)):
    return device_state_repository.get_all_device_states(db)
