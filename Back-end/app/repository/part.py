from sqlalchemy.orm import Session
from app.models.part import PartDB
from app.schemas.part import PartCreate

def create_part(db: Session, part: PartCreate):
    db_part = PartDB(**part.dict())
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

def get_part(db: Session, part_id: int):
    return db.query(PartDB).filter(PartDB.id == part_id).first()

def get_all_parts(db: Session):
    return db.query(PartDB).all()
