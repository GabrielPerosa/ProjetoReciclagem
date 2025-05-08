import uuid
from sqlalchemy.orm import Session
from app.models.part import PartDB
from app.schemas.dto.part import PartDTO
from app.schemas.part import Part

def create_part(db: Session, part_dto: PartDTO) -> Part:
    part = PartDB(
        id=str(uuid.uuid4()),
        type=part_dto.type,
        cycle_id=part_dto.cycle_id
    )
    db.add(part)
    db.commit()
    db.refresh(part)
    return part

def get_all_parts(db: Session) -> list[Part]:
    return db.query(PartDB).all()

def get_quantity_parts(db: Session) -> int:
    return db.query(PartDB).count()

def get_parts_by_type(db: Session, type: str) -> Part | None:
    return db.query(PartDB).filter(PartDB.type == type).all()

def get_quantity_parts_by_type(db: Session, type: str) -> int:
    return db.query(PartDB).filter(PartDB.type == type).count()