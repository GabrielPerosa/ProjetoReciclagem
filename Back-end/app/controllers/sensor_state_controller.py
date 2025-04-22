from fastapi import APIRouter
from models.sensor_state_model import SensorState

router = APIRouter(prefix="/sensor-states")
sensor_states_db = []

@router.get("/")
def list_sensor_states():
    return sensor_states_db

@router.post("/")
def create_sensor_state(data: SensorState):
    sensor_states_db.append(data)
    return {"message": "Created successfully"}
