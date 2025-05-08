from pydantic import BaseModel

class Part(BaseModel):
    id: str
    type: str
    cycle_id: str

    class Config:
        orm_mode = True
