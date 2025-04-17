from fastapi import FastAPI
from controllers import user_controller, ciclo_controller, part_controller, workstation_controller

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(ciclo_controller.router)
app.include_router(part_controller.router)
app.include_router(workstation_controller.router)


@app.get("/")
def root():
    return {"message": "Welcome to the API!"}
