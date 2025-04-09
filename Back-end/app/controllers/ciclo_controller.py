from fastapi import APIRouter
from models.ciclo_model import Ciclo

router = APIRouter(prefix="/ciclos")
ciclos_db = []

@router.get("/")
def list_ciclos():
    return ciclos_db

@router.put("/update/{ciclo_id}")
def update_ciclo(ciclo_id: int, data: Ciclo):
    for i, ciclo in enumerate(ciclos_db):
        if ciclo.id == ciclo_id:
            ciclos_db[i] = data
            return {"message": "Ciclo atualizado com sucesso"}
    return {"message": "Ciclo não encontrado"}
