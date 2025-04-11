from fastapi import FastAPI
from controllers import user_controller, ciclo_controller, peca_controller, estacao_controller

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(ciclo_controller.router)
app.include_router(peca_controller.router)
app.include_router(estacao_controller.router)


@app.get("/")
def root():
    return {"message": "Bem-vindo à API!"}
