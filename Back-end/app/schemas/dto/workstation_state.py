from pydantic import BaseModel
from datetime import datetime

class WorkstationStateDTO(BaseModel):
    state: str
    timestamp: datetime
    workstation_id: str