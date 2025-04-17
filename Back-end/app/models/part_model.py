from pydantic import BaseModel

class Part(BaseModel):
    tipo: str
    id: int