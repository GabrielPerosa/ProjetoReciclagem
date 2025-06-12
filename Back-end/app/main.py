from fastapi import FastAPI
from app.routes.router import router
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app = FastAPI()
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the API!"}
