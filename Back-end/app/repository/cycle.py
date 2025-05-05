from sqlalchemy.orm import Session
from app.models.cycle import CycleDB
from app.schemas.cycle import CycleCreate

def create_cycle(db: Session, cycle: CycleCreate):
    db_cycle = CycleDB(**cycle.dict())
    db.add(db_cycle)
    db.commit()
    db.refresh(db_cycle)
    return db_cycle

def get_cycle(db: Session, cycle_id: int):
    return db.query(CycleDB).filter(CycleDB.id == cycle_id).first()

def get_all_cycles(db: Session):
    return db.query(CycleDB).all()
