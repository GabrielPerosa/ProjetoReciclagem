from pydantic import BaseModel 
from typing import List

class Station(BaseModel):
    id: str
    description: str
    states: List[int] = []
    
    class Config:
        orm_mode = True