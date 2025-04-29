"""
from fastapi import APIRouter
from app.models.workstation import Workstation

router = APIRouter(prefix="/workstations")
workstations_db = []

@router.get("/")
def list_workstations():
    return workstations_db

@router.post("/")
def create_workstation(data: Workstation):
    workstations_db.append(data)
    return {"message": "Created successfully"}
"""
