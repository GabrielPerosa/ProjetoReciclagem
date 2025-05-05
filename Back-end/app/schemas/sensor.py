from pydantic import BaseModel

class SensorDTO(BaseModel):
    id: str
    description: str
    
    class Config:
        orm_mode = True