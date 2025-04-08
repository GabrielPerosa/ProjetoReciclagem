from fastapi import APIRouter, HTTPException
from app.models.dispositivo import Dispositivo
from app.database.fake_db import dispositivos

router = APIRouter(prefix="/dispositivos", tags=["Dispositivos"])

@router.post("/")
def cadastrar_dispositivo(dispositivo: Dispositivo):
    novo_id = max(dispositivos.keys(), default=0) + 1
    dispositivos[novo_id] = dispositivo.dict()
    return {"id": novo_id, "dados": dispositivos[novo_id]}

@router.get("/")
def listar_dispositivos():
    return dispositivos

@router.get("/{id_dispositivo}")
def pegar_dispositivo(id_dispositivo: int):
    if id_dispositivo in dispositivos:
        return dispositivos[id_dispositivo]
    else:
        raise HTTPException(status_code=404, detail="Dispositivo não encontrado")
