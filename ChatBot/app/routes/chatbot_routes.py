from fastapi import APIRouter
from app.controllers.chatbot_controller import ChatbotController, MessageRequest

router = APIRouter()
controller = ChatbotController()

@router.post("/chat")
async def chat(request: MessageRequest):
    return await controller.handle_message(request)