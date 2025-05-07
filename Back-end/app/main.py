from fastapi import FastAPI
from app.routes import auth, cycle, part, sensor, sensor_state, user, workstation, workstation_state

app = FastAPI()

app.include_router(user.router)
app.include_router(cycle.router)
app.include_router(part.router)
app.include_router(workstation.router)
app.include_router(workstation_state.router)
app.include_router(sensor.router)
app.include_router(sensor_state.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Welcome to the API!"}
