from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import User
from app.schemas.dto.user import UserDTO
from app.repository import user as user_repository
from app.config.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User)
def create(user_dto: UserDTO, db: Session = Depends(get_db)):
    existing = user_repository.get_user_by_email(db, user_dto.email)
    if existing:
        raise HTTPException(status_code=400, detail="E-mail already registered")
    return user_repository.create_user(db, user_dto)

@router.get("/", response_model=list[User])
def list_all(db: Session = Depends(get_db)):
    return user_repository.get_all_users(db)

@router.put("/password/{user_id}", response_model=User)
def update_password(user_id: str, new_password: str, db: Session = Depends(get_db)):
    user = user_repository.update_user_password(db, user_id, new_password)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
