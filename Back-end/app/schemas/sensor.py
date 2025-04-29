from pydantic import BaseModel

class Sensor(BaseModel):
    description: str
    
    class Config:
        orm_mode = True