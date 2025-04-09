from fastapi import APIRouter
from models.user_model import User, UserBase
import uuid

router = APIRouter(prefix="/users")

users_db = []

@router.get("/")
def list_users():
    return users_db

@router.post("/create", response_model=User)
def create_user(user_data: UserBase):
    user = User(id=str(uuid.uuid4()), **user_data.dict())
    users_db.append(user)
    return user

@router.put("update-password/{user_id}")
def update_password(user_id: str, new_password: str):
    for user in users_db:
        if user.id == user_id:
            user.password = new_password
            return {"message": "Senha atualizada com sucesso!"}