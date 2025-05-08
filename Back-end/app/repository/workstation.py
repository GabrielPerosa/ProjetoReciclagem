import uuid
from sqlalchemy.orm import Session
from app.models.workstation import WorkstationDB
from app.schemas.dto.workstation import WorkstationDTO
from app.schemas.workstation import Workstation

def create_workstation(db: Session, workstation_dto: WorkstationDTO) -> Workstation:
    workstation = WorkstationDB(
        id=str(uuid.uuid4()),
        description=workstation_dto.description
    )
    db.add(workstation)
    db.commit()
    db.refresh(workstation)
    return workstation

def get_all_workstations(db: Session) -> list[Workstation]:
    return db.query(WorkstationDB).all()
