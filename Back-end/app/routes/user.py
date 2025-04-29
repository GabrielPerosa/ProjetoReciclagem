from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate
from app.repository.user import create_user, get_users, update_user_password
from app.config.database import get_db
from typing import List

router = APIRouter(prefix="/users")

@router.get("/", response_model=List[User])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.put("/update-password/{user_id}")
def update_password(user_id: str, new_password: str, db: Session = Depends(get_db)):
    updated = update_user_password(db, user_id, new_password)
    if not updated:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Senha atualizada com sucesso!"}
