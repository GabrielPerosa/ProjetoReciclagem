from pydantic import BaseModel
from datetime import datetime

class Ciclo(BaseModel):
    id: int
    tempo_inicial: datetime
    tempo_final: datetime
    peca_id: int
