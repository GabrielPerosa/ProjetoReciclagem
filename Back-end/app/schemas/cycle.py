from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Cycle(BaseModel):
    id: int
    initial_time: Optional[datetime]
    end_time: Optional[datetime]
    
    class Config:
        orm_mode = True
