from fastapi import APIRouter
from models.peca_model import Peca

router = APIRouter(prefix="/pecas")
pecas_db = []

@router.get("/")
def list_pecas():
    return pecas_db

@router.put("/update/{peca_id}")
def update_peca(peca_id: int, data: Peca):
    for i, peca in enumerate(pecas_db):
        if peca.id == peca_id:
            pecas_db[i] = data
            return {"message": "Peça atualizada com sucesso"}
    return {"message": "Peça não encontrada"}
