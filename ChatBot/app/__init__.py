from fastapi import FastAPI
from app.routes.chatbot_routes import router

def create_app():
    app = FastAPI(title="Chatbot API")
    app.include_router(router, prefix="/chat")
    return app