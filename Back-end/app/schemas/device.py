from pydantic import BaseModel
from typing import List

class Device(BaseModel):
    id: str
    description: str
    states: List[int] = []
    
    class Config:
        orm_mode = True