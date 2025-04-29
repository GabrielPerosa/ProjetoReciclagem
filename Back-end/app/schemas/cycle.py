from pydantic import BaseModel
from datetime import datetime

class Cycle(BaseModel):
    initial_time: datetime
    end_time: datetime
    part_id: int

    class Config:
        orm_mode = True