from pydantic import BaseModel
from datetime import datetime

class SensorStateDTO(BaseModel):
    state: str
    timestamp: datetime
    sensor_id: str