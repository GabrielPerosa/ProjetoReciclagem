from pydantic import BaseModel

class PartDTO(BaseModel):
    id: int
    type: str
    cycle_id: int

    class Config:
        orm_mode = True
