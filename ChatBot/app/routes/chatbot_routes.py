from fastapi import APIRouter
import requests
import json
import http
import os
from app.controllers.chatbot_controller import ChatbotController, MessageRequest

router = APIRouter()
controller = ChatbotController()

@router.post("/chat")
async def chat(request: MessageRequest):
    return await controller.handle_message(request)
@router.get("/")
async def health():
    return requests.get(os.getenv("http://localhost:8000/"))
