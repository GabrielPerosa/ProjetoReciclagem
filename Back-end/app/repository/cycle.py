from sqlalchemy.orm import Session
from app.models.cycle import CycleDB
from app.schemas.cycle import Cycle
from typing import List

def create_cycle(db: Session, cycle: Cycle) -> CycleDB:
    db_cycle = CycleDB(
        initial_time=cycle.initial_time,
        end_time=cycle.end_time,
        part_id=cycle.part_id
    )
    db.add(db_cycle)
    db.commit()
    db.refresh(db_cycle)
    return db_cycle

def get_cycles(db: Session) -> List[CycleDB]:
    return db.query(CycleDB).all()