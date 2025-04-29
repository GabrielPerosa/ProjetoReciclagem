from sqlalchemy.orm import Session
from app.models.workstation import Workstation as WorkstationModel
from app.schemas.workstation import Workstation

def create_workstation(db: Session, workstation: Workstation):
    db_workstation = WorkstationModel(
        description=workstation.description
    )
    db.add(db_workstation)
    db.commit()
    db.refresh(db_workstation)
    return db_workstation

def get_workstations(db: Session):
    return db.query(WorkstationModel).all()
