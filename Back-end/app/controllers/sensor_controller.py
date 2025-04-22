from fastapi import APIRouter
from models.sensor_model import Sensor

router = APIRouter(prefix="/sensors")
sensors_db = []

@router.get("/")
def list_sensors():
    return sensors_db

@router.post("/")
def create_sensor(data: Sensor):
    sensors_db.append(data)
    return {"message": "Created successfully"}
