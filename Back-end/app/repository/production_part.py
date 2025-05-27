import uuid
from sqlalchemy.orm import Session
from app.models.production_part import ProductionPartDB
from app.models.part import PartDB
from app.models.cycle import CycleDB
from app.schemas.dto.production_part import ProductionPartDTO
from app.models.station_state import StationStateDB
from datetime import datetime
from sqlalchemy import func

def create_production_part(db: Session, dto: ProductionPartDTO) -> ProductionPartDB:
    part = db.query(PartDB).filter(PartDB.type == dto.part_type).first()
    if not part:
        part = PartDB(id=str(uuid.uuid4()), type=dto.part_type)
        db.add(part)
        db.flush()

    latest_cycle = (
        db.query(CycleDB)
          .join(StationStateDB, StationStateDB.cycle_id == CycleDB.id)
          .order_by(StationStateDB.timestamp.desc())
          .first()
    )
    if not latest_cycle:
        raise Exception("Nenhum ciclo com StationState encontrado. Crie ao menos um station_state primeiro.")

    production_part = ProductionPartDB(
        part_id=part.id,
        stored_quantity=1,
        cycle_id=latest_cycle.id,
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
    
def get_utilization(db: Session) -> int:
    total_non_discard = (
        db.query(func.coalesce(func.sum(ProductionPartDB.stored_quantity), 0))
          .join(PartDB, ProductionPartDB.part_id == PartDB.id)
          .filter(PartDB.type != "descarte")
          .scalar()
    ) or 0
    
    total_discard = (
        db.query(func.coalesce(func.sum(ProductionPartDB.stored_quantity), 0))
          .join(PartDB, ProductionPartDB.part_id == PartDB.id)
          .filter(PartDB.type == "descarte")
          .scalar()
    ) or 0

    return total_non_discard - total_discard

def get_total_quantity_by_part_type(db: Session, part_type: str) -> dict:
    total_quantity = (
        db.query(func.coalesce(func.sum(ProductionPartDB.stored_quantity), 0))
        .join(PartDB, ProductionPartDB.part_id == PartDB.id)
        .filter(PartDB.type == part_type)
        .scalar()
    )
    return {
        "part_type": part_type,
        "total_quantity": total_quantity
    }

def get_production_summary(db: Session) -> dict:
    results = (
        db.query(
            PartDB.type,
            func.date(StationStateDB.timestamp).label("date"),
            func.to_char(StationStateDB.timestamp, 'HH24:MI').label("time"),
            func.sum(ProductionPartDB.stored_quantity).label("quantity")
        )
        .join(PartDB, ProductionPartDB.part_id == PartDB.id)
        .join(CycleDB, ProductionPartDB.cycle_id == CycleDB.id)
        .join(StationStateDB, StationStateDB.cycle_id == CycleDB.id)
        .group_by(PartDB.type, func.date(StationStateDB.timestamp), func.to_char(StationStateDB.timestamp, 'HH24:MI'))
        .order_by(func.date(StationStateDB.timestamp), func.to_char(StationStateDB.timestamp, 'HH24:MI'))
        .all()
    )

    summary = {}
    material_types = set()

    for part_type, date, time, quantity in results:
        material_types.add(part_type)
        date_str = str(date)
        if part_type not in summary:
            summary[part_type] = {}
        if date_str not in summary[part_type]:
            summary[part_type][date_str] = {}
        summary[part_type][date_str][time] = quantity

    summary["material"] = list(material_types)

    return summary