from pydantic import BaseModel
from datetime import datetime

class WorkstationState(BaseModel):
    id: int
    state: str
    timestamp: datetime
    workstation_id: int
