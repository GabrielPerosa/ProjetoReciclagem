from sqlalchemy.orm import Session
from app.models.part import PartDB
from app.schemas.dto.part import PartDTO
from app.schemas.part import Part

def create_part(db: Session, part_dto: PartDTO) -> Part:
    part = PartDB(
        type=part_dto.type,
        cycle_id=part_dto.cycle_id
    )
    db.add(part)
    db.commit()
    db.refresh(part)
    return part

def get_all_parts(db: Session) -> list[Part]:
    return db.query(PartDB).all()