from fastapi import APIRouter, HTTPException
from app.models.usuario import Usuario
from app.database.fake_db import usuarios

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post("/")
def cadastrar_usuario(usuario: Usuario):
    novo_id = max(usuarios.keys(), default=0) + 1
    usuarios[novo_id] = usuario.dict()
    return {"id": novo_id, "dados": usuarios[novo_id]}

@router.get("/")
def listar_usuarios():
    return usuarios

@router.get("/{id_usuario}")
def pegar_usuario(id_usuario: int):
    if id_usuario in usuarios:
        return usuarios[id_usuario]
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.put("/{id_usuario}")
def atualizar_usuario(id_usuario: int, usuario: Usuario):
    if id_usuario not in usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    usuarios[id_usuario] = usuario.dict()
    return {"id": id_usuario, "dados": usuarios[id_usuario]}

@router.delete("/{id_usuario}")
def deletar_usuario(id_usuario: int):
    if id_usuario not in usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    del usuarios[id_usuario]
    return {"message": f"Usuário {id_usuario} removido com sucesso"}
