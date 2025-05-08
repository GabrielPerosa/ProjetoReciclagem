from pydantic import BaseModel

class Sensor(BaseModel):
    id: str
    description: str
    
    class Config:
        orm_mode = True