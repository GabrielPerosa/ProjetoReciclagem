from pydantic import BaseModel
from typing import List
from .device_state import DeviceState

class Device(BaseModel):
    id: str
    description: str
    states: List[DeviceState] = []
    
    class Config:
        orm_mode = True