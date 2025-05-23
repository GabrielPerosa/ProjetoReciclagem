from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ProductionPart(BaseModel):
    id: str
    part_id: str
    stored_quantity: int 
    cycle_id: str
    
    class Config:
        orm_mode = True
        
class ProductionPartWithTimestamp(ProductionPart):
    part_type: str
    timestamp: Optional[datetime]

    class Config(ProductionPart.Config):
        pass
