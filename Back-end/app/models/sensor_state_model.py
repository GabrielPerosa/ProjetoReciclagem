from pydantic import BaseModel
from datetime import datetime

class SensorState(BaseModel):
    id: int
    state: bool
    timestamp: datetime
    sensor_id: int
