from pydantic import BaseModel

class Workstation(BaseModel):
    id: str
    description: str
    
    class Config:
        from_attributes = True