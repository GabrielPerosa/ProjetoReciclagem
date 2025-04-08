from pydantic import BaseModel

class Usuario(BaseModel):
    senha: int
    nome: str
    email: str
