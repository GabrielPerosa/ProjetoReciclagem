from pydantic import BaseModel

class ProductionPartDTO(BaseModel):
    part_id: str
    part_type: str
    stored_quantity: int