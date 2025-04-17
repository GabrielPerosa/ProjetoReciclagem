from fastapi import APIRouter
from models.cycle_model import Cycle

router = APIRouter(prefix="/cycles")
cycles_db = []

@router.get("/")
def list_cycles():
    return cycles_db

@router.post("/update/{cycle_id}")
def update_cycle(cycle_id: int, data: Cycle):
    for i, cycle in enumerate(cycles_db):
        if cycle.id == cycle_id:
            cycles_db[i] = data
            return {"message": "Cycle updated successfully"}
    return {"message": "Cycle not found"}
