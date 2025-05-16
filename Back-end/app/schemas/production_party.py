from pydantic import BaseModel

class ProductionParty(BaseModel): 
    id: str
    stored_part_id: str 
    cycle_id: str
    
    class Config:
        orm_mode = True