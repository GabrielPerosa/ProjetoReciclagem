from pydantic import BaseModel

class StationDTO(BaseModel):
    description: str
    