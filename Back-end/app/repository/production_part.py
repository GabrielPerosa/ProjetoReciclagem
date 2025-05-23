import uuid
from sqlalchemy.orm import Session
from app.models.production_part import ProductionPartDB
from app.models.part import PartDB
from app.models.cycle import CycleDB
from app.schemas.dto.production_part import ProductionPartDTO
from app.models.station_state import StationStateDB
from datetime import datetime

def create_production_part(db: Session, dto: ProductionPartDTO) -> ProductionPartDB:
    part = db.query(PartDB).filter(PartDB.type == dto.part_type).first()

    if not part:
        part = PartDB(
            id=str(uuid.uuid4()),
            type=dto.part_type,
        )
        db.add(part)
        db.flush()

    cycle = CycleDB(id=str(uuid.uuid4()))
    db.add(cycle)
    db.flush()

    production_part = ProductionPartDB(
        part_id=part.id,
        stored_quantity=dto.stored_quantity,
        cycle_id=cycle.id,
    )
    db.add(production_part)
    db.commit()
    db.refresh(production_part)
    return production_part

def get_parts_by_type_with_timestamp(db: Session,part_type: str) -> list[tuple[str, str, str, int, str, datetime]]:
    return (
        db.query(
            ProductionPartDB.id,
            ProductionPartDB.part_id,
            ProductionPartDB.cycle_id,
            ProductionPartDB.stored_quantity,
            PartDB.type.label("part_type"),
            StationStateDB.timestamp,
        )
        .join(PartDB, ProductionPartDB.part_id == PartDB.id)
        .join(CycleDB, ProductionPartDB.cycle_id == CycleDB.id)
        .outerjoin(StationStateDB, StationStateDB.cycle_id == CycleDB.id)
        .filter(PartDB.type == part_type)
        .all()
    )