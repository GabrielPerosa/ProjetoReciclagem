from sqlalchemy.orm import Session
from app.models.user import UserDB
from app.schemas.dto.user import UserDTO
from app.schemas.user import User
from app.auth.security import hash_password
import uuid

def create_user(db: Session, user_dto: UserDTO) -> User:
    user_db = UserDB(
        id=str(uuid.uuid4()),
        name=user_dto.name,
        email=user_dto.email,
        password=hash_password(user_dto.password)
    )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(UserDB).filter(UserDB.email == email).first()

def get_all_users(db: Session) -> list[User]:
    return db.query(UserDB).all()

def update_user_password(db: Session, user_id: str, new_password: str) -> User | None:
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if user:
        user.password = hash_password(new_password)
        db.commit()
        db.refresh(user)
    return user
