from fastapi import APIRouter
import httpx
import os
from app.controllers.chatbot_controller import ChatbotController, MessageRequest

router = APIRouter()
controller = ChatbotController()

@router.post("/chat")
async def chat(request: MessageRequest):
    return await controller.handle_message(request)
@router.get("/health")
async def health():
    async with httpx.AsyncClient() as client:
        r = await client.get(os.environ.get("API_URL"))
        return r.status_code
