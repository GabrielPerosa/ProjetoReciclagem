from pydantic import BaseModel

class Workstation(BaseModel):
    id: int
    description: str