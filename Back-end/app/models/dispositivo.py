from pydantic import BaseModel

class Dispositivo(BaseModel):
    tipo: str
    nome: str
