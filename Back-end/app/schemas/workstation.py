from pydantic import BaseModel

class WorkstationDTO(BaseModel):
    id: str
    description: str
    
    class Config:
        from_attributes = True