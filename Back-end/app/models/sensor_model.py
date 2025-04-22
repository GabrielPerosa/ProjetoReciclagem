from pydantic import BaseModel

class Sensor(BaseModel):
    id: int
    description: str