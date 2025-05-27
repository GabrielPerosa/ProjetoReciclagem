from pydantic import BaseModel
from typing import List
from datetime import datetime
from uuid import UUID

class Part(BaseModel):
    id: str
    type: str
    productions: List[int] = []

    class Config:
        orm_mode = True
