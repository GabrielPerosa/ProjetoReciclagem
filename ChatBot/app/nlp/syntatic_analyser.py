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
            tokens = set(message_clean.split())

            scores = {}

            for intent, keywords in self.intents.items():
                keywords_matched = sum(1 for kw in keywords if self.parse_message(kw) in tokens)
                if keywords_matched:
                    scores[intent] = keywords_matched

            if scores:
                # Retorna a intent com mais correspondências
                best_intent = max(scores, key=scores.get)
                print(f"Intenção detectada: {best_intent} com {scores[best_intent]} palavras-chave")
                return best_intent

            return "default"

    def _extract_entities(self, message: str) -> Dict[str, List[str]]:
            """Extrai entidades usando regex."""
            entities = {"date": [], "hour": [], "material": []}
            message_normalized = self.parse_message(message)           
           
            # Extração com regex
            for entity_name, config in self.entities.items():
                for pattern in config["patterns"]:
                    matches = re.finditer(pattern, message_normalized, re.IGNORECASE)
                    for match in matches:
                        print(f"Entidade {entity_name} encontrada: {match.group(0)}")
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
    