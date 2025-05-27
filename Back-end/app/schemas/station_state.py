from pydantic import BaseModel 
from datetime import datetime

class StationState(BaseModel):
    id: str
    station_id: str
    cycle_id: str
    state: bool
    timestamp: datetime
    
    class Config:
        orm_mode = True