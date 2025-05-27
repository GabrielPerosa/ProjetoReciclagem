import uuid
from app.auth.jwt import create_access_token
from app.auth.security import verify_password
from app.repository.user import get_user_by_email
from sqlalchemy.orm import Session
from app.schemas.dto.login import LoginDTO
from http.client import HTTPException

def login_user(db: Session, dto: LoginDTO) -> dict:
    user = get_user_by_email(db, dto.email)
    if not user or not verify_password(dto.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
