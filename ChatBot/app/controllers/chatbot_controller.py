from app.services.chatbot_service import ChatbotService
from pydantic import BaseModel
from typing import Dict, Any

class MessageRequest(BaseModel):
    message: str

class ChatbotController:
    def __init__(self):
        self.service = ChatbotService()

    async def handle_message(self, request: MessageRequest) -> Dict[str, Any]:
        return await self.service.get_response(request.message)
