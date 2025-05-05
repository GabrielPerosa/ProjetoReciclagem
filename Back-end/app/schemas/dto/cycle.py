from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Cycle(BaseModel):
    initial_time: Optional[datetime]
    end_time: Optional[datetime]