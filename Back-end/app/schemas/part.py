from pydantic import BaseModel
from typing import List
from datetime import datetime

class Part(BaseModel):
    id: str
    type: str
    cycle_id: str

    class Config:
        orm_mode = True
