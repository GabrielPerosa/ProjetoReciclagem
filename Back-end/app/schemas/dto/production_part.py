from pydantic import BaseModel

class ProductionPartDTO(BaseModel): 
    stored_part_id: str 
    cycle_id: str