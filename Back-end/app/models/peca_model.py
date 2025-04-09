from pydantic import BaseModel

class Peca(BaseModel):
    tipo: str
    id: int