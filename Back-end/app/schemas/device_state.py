from pydantic import BaseModel
from datetime import datetime

class DeviceState(BaseModel):
    id: str
    device_id: str
    state: bool
    timestamp: datetime
    
    class Config:
        orm_mode = True