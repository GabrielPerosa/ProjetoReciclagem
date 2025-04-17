from pydantic import BaseModel

class Part(BaseModel):
    type: str
    id: int