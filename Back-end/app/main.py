from fastapi import FastAPI
from app.routes import dispositivo, usuario

app = FastAPI(title="Minha API", description="Uma API de teste", version="1.0")

app.include_router(dispositivo.router)
app.include_router(usuario.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
