from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CycleBase(BaseModel):
    initial_time: Optional[datetime]
    end_time: Optional[datetime]
    part_id: int

class CycleCreate(CycleBase):
    pass

class Cycle(CycleBase):
    id: int

    class Config:
        orm_mode = True
