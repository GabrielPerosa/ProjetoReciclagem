from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.dto.login import LoginDTO
from app.repository import auth as auth_service
from app.config.database import get_db

router = APIRouter(prefix="/login", tags=["Login"])
@router.post("/")
def login(dto: LoginDTO, db: Session = Depends(get_db)):
    return auth_service.login_user(db, dto)
