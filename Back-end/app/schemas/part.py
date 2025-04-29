from pydantic import BaseModel

class Part(BaseModel):
    type: str
    
    class Config:
        orm_mode = True