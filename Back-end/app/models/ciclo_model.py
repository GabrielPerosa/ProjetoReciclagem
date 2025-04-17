from pydantic import BaseModel
from datetime import datetime

class Ciclo(BaseModel):
    id: int
    initial_time: datetime
    end_time: datetime
    part_id: int
