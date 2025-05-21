import uuid
from sqlalchemy.orm import Session
from app.models.production_part import ProductionPartDB
from app.models.part import PartDB
from app.models.cycle import CycleDB
from app.schemas.dto.production_part import ProductionPartDTO

def create_production_part(db: Session, dto: ProductionPartDTO) -> ProductionPartDB:
    # Cria a peça
    part = PartDB(
        id=str(uuid.uuid4()),
        type=dto.part_type,
    )
    db.add(part)
    db.flush()

    # Sempre cria um novo ciclo
    cycle = CycleDB(id=str(uuid.uuid4()))
    db.add(cycle)
    db.flush()

    # Cria a relação de produção da peça com o ciclo
    production_part = ProductionPartDB(
        part_id=part.id,
        stored_quantity=dto.stored_quantity,
        cycle_id=cycle.id,
    )
    db.add(production_part)
    db.commit()
    db.refresh(production_part)
    return production_part
