from pydantic import BaseModel

class PartDTO(BaseModel):
    type: str
    cycle_id: int