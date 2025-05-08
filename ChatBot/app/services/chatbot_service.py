from app.nlp.nlp_processor import NLPProcessor
from typing import Dict, Any

class ChatbotService:
    def __init__(self):
        self.nlp_processor = NLPProcessor()

    async def get_response(self, message: str) -> Dict[str, Any]:
        return self.nlp_processor.process_message(message)