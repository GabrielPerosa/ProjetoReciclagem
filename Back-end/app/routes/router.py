from fastapi import APIRouter
from app.routes import auth, cycle, part, sensor, sensor_state, user, workstation, workstation_state

router = APIRouter()

router.include_router(user.router)
router.include_router(cycle.router)
router.include_router(part.router)
router.include_router(workstation.router)
router.include_router(workstation_state.router)
router.include_router(sensor.router)
router.include_router(sensor_state.router)
router.include_router(auth.router)
