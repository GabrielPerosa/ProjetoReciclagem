from pydantic import BaseModel
from datetime import datetime

class DeviceStateDTO(BaseModel):
    device_id: str
    state: bool
    timestamp: datetime