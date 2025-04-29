"""
from fastapi import APIRouter
from app.models.workstation_state import WorkstationState

router = APIRouter(prefix="/workstation_state")
states_db = []

@router.get("/")
def list_workstation_states():
    return states_db

@router.post("/")
def create_workstation_state(data: WorkstationState):
    states_db.append(data)
    return {"message": "State created successfully"}
"""
