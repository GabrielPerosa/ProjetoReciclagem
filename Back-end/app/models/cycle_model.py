from pydantic import BaseModel
from datetime import datetime

class Cycle(BaseModel):
    id: int
    initial_time: datetime
    end_time: datetime
    part_id: int
