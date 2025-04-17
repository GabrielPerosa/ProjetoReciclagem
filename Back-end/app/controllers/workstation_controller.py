from fastapi import APIRouter
from models.workstation_model import Workstation

router = APIRouter(prefix="/workstations")
workstations_db = []

@router.get("/")
def list_workstations():
    return workstations_db

@router.post("/update/{workstation_id}")
def update_workstation(workstation_id: int, data: Workstation):
    for i, est in enumerate(workstations_db):
        if est.id == workstation_id:
            workstations_db[i] = data
            return {"message": "Workstation updated successfully"}
    return {"message": "Workstation not found"}