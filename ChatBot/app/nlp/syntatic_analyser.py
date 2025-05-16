import re
from typing import Dict, List
import unicodedata
from app.services.load_data import load_data

class SyntaticAnalyzer:
    def __init__(self):
        self.intents = load_data('app/data/intents.json')
        self.entities = load_data('app/data/entities.json')
        self.continuation_keywords = ["e", "além disso", "outra", "mais", "também"]

    def parse_message(self, message: str):
        """Normaliza a mensagem para facilitar a comparação."""
        message = message.lower()
        message = unicodedata.normalize('NFKD', message).encode('ASCII', 'ignore').decode('utf-8')
        return message.strip()
        
    def _detect_intent(self, message: str) -> str:
            """Detecta a intenção com base em palavras-chave definidas."""
            message_normalized = self.parse_message(message)
            message_clean = re.sub(r'[^\w\s]', '', message_normalized)
            
            for intent, keywords in self.intents.items():
                for keyword in keywords:
                    keyword_normalized = self.parse_message(keyword)
                    if keyword_normalized in message_clean:
                        print(f"Intenção detectada: {intent} com a palavra-chave: {keyword}")
                        return intent
            return "default"

    def _extract_entities(self, message: str) -> Dict[str, List[str]]:
            """Extrai entidades usando regex e spaCy."""
            entities = {"codigo": [], "quantidade": [], "material": [], "taxa": []}
            message_normalized = self.parse_message(message)           
           
            # Extração com regex
            for entity_name, config in self.entities.items():
                for pattern in config["patterns"]:
                    matches = re.finditer(pattern, message_normalized, re.IGNORECASE)
                    for match in matches:
                        if config["grupo"] is not None:
                            value = match.group(config["grupo"])
                        else:
                            value = match.group(0)
                        entities[entity_name].append(value)
            
            # Remover duplicatas
            for key in entities:
                entities[key] = list(set(entities[key]))
            print(entities)
            return entities
    