import uuid
from sqlalchemy.orm import Session
from app.models.production_part import ProductionPartDB
from app.schemas.dto.production_part import ProductionPartDTO

def create_production_part(db: Session, production_part_dto: ProductionPartDTO) -> ProductionPartDB:
    production_part = ProductionPartDB(
        id=str(uuid.uuid4()),
        stored_part_id=production_part_dto.stored_part_id,
        cycle_id=production_part_dto.cycle_id,
    )
    db.add(production_part)
    db.commit()
    db.refresh(production_part)
    return production_part

def get_all_production_parts(db: Session) -> list[ProductionPartDB]:
    return db.query(ProductionPartDB).all()
