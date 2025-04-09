from fastapi import FastAPI
from controllers import user_controller

app = FastAPI()

app.include_router(user_controller.router)

@app.get("/")
def root():
    return {"message": "Bem-vindo à API!"}
