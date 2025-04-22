from pydantic import BaseModel
from datetime import datetime

class WorkstationState(BaseModel):
    id: int
    state: bool
    timestamp: datetime
    workstation_id: int
