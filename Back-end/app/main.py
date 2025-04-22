from fastapi import FastAPI
from controllers import user_controller, cycle_controller, part_controller, workstation_controller, workstation_state_controller,sensor_controller, sensor_state_controller

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(cycle_controller.router)
app.include_router(part_controller.router)
app.include_router(workstation_controller.router)
app.include_router(workstation_state_controller.router)
app.include_router(sensor_controller.router)
app.include_router(sensor_state_controller.router)


@app.get("/")
def root():
    return {"message": "Welcome to the API!"}
