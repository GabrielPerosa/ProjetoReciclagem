from fastapi import APIRouter
from models.estacao_model import Estacao

router = APIRouter(prefix="/estacoes")
estacoes_db = []

@router.get("/")
def list_estacoes():
    return estacoes_db

@router.put("/update/{estacao_id}")
def update_estacao(estacao_id: int, data: Estacao):
    for i, est in enumerate(estacoes_db):
        if est.id == estacao_id:
            estacoes_db[i] = data
            return {"message": "Estação atualizada com sucesso"}
    return {"message": "Estação não encontrada"}