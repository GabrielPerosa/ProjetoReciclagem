from pydantic import BaseModel
from datetime import datetime

class WorkstationState(BaseModel):
    id: str
    state: str
    timestamp: datetime
    workstation_id: int

    class Config:
        from_attributes = True