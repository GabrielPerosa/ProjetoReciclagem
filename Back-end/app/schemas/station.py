from pydantic import BaseModel 
from typing import List
from .station_state import StationState

class Station(BaseModel):
    id: str
    description: str
    states: List[StationState] = []
    
    class Config:
        orm_mode = True