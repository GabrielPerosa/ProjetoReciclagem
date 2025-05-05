from pydantic import BaseModel

class Part(BaseModel):
    type: str
    cycle_id: int