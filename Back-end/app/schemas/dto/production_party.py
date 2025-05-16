from pydantic import BaseModel

class ProductionPartyDTO(BaseModel): 
    stored_part_id: str 
    cycle_id: str