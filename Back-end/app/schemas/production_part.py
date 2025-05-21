from pydantic import BaseModel

class ProductionPart(BaseModel):
    id: str
    part_id: str
    stored_quantity: int 
    cycle_id: str
    
    class Config:
        orm_mode = True