from pydantic import BaseModel 
from datetime import datetime

class StationStateDTO(BaseModel):
    station_id: str
    cycle_id: str
    state: bool
    timestamp: datetime