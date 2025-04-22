from fastapi import APIRouter
from models.cycle_model import Cycle

router = APIRouter(prefix="/cycles")
cycles_db = []

@router.get("/")
def list_cycles():
    return cycles_db

@router.post("/")
def create_cycle(data: Cycle):
    cycles_db.append(data)
    return {"message": "Created successfully"}
