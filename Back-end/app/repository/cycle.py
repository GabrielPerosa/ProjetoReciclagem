from sqlalchemy.orm import Session
from app.models.cycle import CycleDB
from app.schemas.dto.cycle import CycleDTO
from app.schemas.cycle import Cycle

def create_cycle(db: Session, cycle_dto: CycleDTO) -> Cycle:
    cycle = CycleDB(
        initial_time=cycle_dto.initial_time,
        end_time=cycle_dto.end_time
    )
    db.add(cycle)
    db.commit()
    db.refresh(cycle)
    return cycle

def get_all_cycles(db: Session) -> list[Cycle]:
    return db.query(CycleDB).all()
