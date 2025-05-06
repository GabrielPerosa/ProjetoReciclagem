from pydantic import BaseModel

class Part(BaseModel):
    id: int
    type: str
    cycle_id: int

    class Config:
        orm_mode = True
