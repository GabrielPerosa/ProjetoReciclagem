import uuid
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.part import PartDB
from app.schemas.dto.part import PartDTO

def create_part(db: Session, part_dto: PartDTO) -> PartDB:
    part = PartDB(
        id=str(uuid.uuid4()),
        type=part_dto.type,
    )
    db.add(part)
    db.commit()
    db.refresh(part)
    return part

def list_parts_with_quantity(db: Session) -> list[tuple[PartDB, int]]:
    return (
        db.query(PartDB, func.count(PartDB.id).label("quantity"))
          .group_by(PartDB.id, PartDB.type)
          .all()
    )

def get_quantity(db: Session, type: str) -> int:
    count = (
        db.query(func.count(PartDB.id))
          .filter(PartDB.type == type)
          .scalar()
    )
    return count or 0