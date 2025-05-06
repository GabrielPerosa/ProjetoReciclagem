from pydantic import BaseModel
from datetime import datetime

class SensorState(BaseModel):
    id: str
    state: str
    timestamp: datetime
    sensor_id: int

class Config:
        orm_mode = True