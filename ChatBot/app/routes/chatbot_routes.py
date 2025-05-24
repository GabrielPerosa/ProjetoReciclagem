from fastapi import APIRouter
import httpx
import os
from app.controllers.chatbot_controller import ChatbotController, MessageRequest

router = APIRouter()
controller = ChatbotController()

@router.post("/prompt")
async def chat(request: MessageRequest):
    return await controller.handle_message(request)
#@router.get("/health")
#async def health():
#    async with httpx.AsyncClient(timeout=3.0) as client:
#        r = await client.get("http://{}".format(os.environ.get("API_URL")))
#        if r.status_code == 200:
#            return {"status": "healthy", "api_status": r.status_code}
#        else:
#            return {"status": "unhealthy", "api_status": r.status_code}
    