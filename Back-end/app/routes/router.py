from fastapi import APIRouter
from app.routes import auth, device_state, device, part, production_part, station_state, station, user

router = APIRouter()

router.include_router(auth.router)
router.include_router(device_state.router)
router.include_router(device.router)
router.include_router(part.router)
router.include_router(production_part.router)
router.include_router(station_state.router)
router.include_router(station.router)
router.include_router(user.router)