from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.workstation import Workstation
from app.schemas.dto.workstation import WorkstationDTO
from app.repository import workstation as workstation_repository
from app.config.database import get_db

router = APIRouter(prefix="/workstations", tags=["Workstations"])

@router.post("/", response_model=Workstation)
def create(workstation_dto: WorkstationDTO, db: Session = Depends(get_db)):
    return workstation_repository.create_workstation(db, workstation_dto)

@router.get("/", response_model=list[Workstation])
def list_all(db: Session = Depends(get_db)):
    return workstation_repository.get_all_workstations(db)
