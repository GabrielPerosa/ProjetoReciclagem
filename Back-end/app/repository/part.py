from sqlalchemy.orm import Session
from app.models.part import PartDB
from app.schemas.part import Part
from typing import List

def create_part(db: Session, part: Part) -> PartDB:
    db_part = PartDB(
        type=part.type
    )
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

def get_parts(db: Session) -> List[PartDB]:
    return db.query(PartDB).all()
