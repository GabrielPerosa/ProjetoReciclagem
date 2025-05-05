from pydantic import BaseModel
from datetime import datetime

class WorkstationState(BaseModel):
    state: str
    timestamp: datetime
    workstation_id: int