from pydantic import BaseModel

class Estacao(BaseModel):
    id: int
    descricao: str