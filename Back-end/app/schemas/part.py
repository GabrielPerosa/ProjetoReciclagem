from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Cycle(BaseModel):
    id: int
    initial_time: Optional[datetime]
    end_time: Optional[datetime]
    part_id: int

    class Config:
        orm_mode = True

class PartBase(BaseModel):
    type: str

class PartCreate(PartBase):
    pass

class Part(PartBase):
    id: int
    cycles: List[Cycle] = []

    class Config:
        orm_mode = True
