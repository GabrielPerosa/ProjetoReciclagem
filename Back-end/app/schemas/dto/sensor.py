from pydantic import BaseModel

class SensorDTO(BaseModel):
    description: str