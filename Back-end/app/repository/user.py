import uuid
from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate

def get_users(db: Session):
    return db.query(UserModel).all()

def create_user(db: Session, user: UserCreate):
    db_user = UserModel(
        id=str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_password(db: Session, user_id: str, new_password: str):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        user.password = new_password
        db.commit()
        db.refresh(user)
        return user
    return None
