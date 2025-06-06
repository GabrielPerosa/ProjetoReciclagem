import re
from typing import Dict, List
import unicodedata
from app.utils.load_data import load_data

class SyntaticAnalyzer:
    def __init__(self):
        self.intents = load_data('app/data/intents.json')
        self.entities = load_data('app/data/entities.json')

    def parse_message(self, message: str):
        """Normaliza a mensagem para facilitar a comparação."""
        message = message.lower()
        message = unicodedata.normalize('NFKD', message).encode('ASCII', 'ignore').decode('utf-8')
        return message.strip()
        
    def pre_proc_message(self, message: str):
        message_normalized = self.parse_message(message)
        message_clean = re.sub(r'[^\w\s]', '', message_normalized)
        return message_clean.strip().split()
    
    def _detect_intent(self, message: str) -> str:
            """Detecta a intenção com base em palavras-chave definidas."""
            message_tokens = self.pre_proc_message(message)
            
            scores = {}
            for intent, keywords in self.intents.items():
                result = 0
                for kw in keywords:
                    kw = self.parse_message(kw)
                    tokens = kw.split()

                    # Verifica se todos os tokens da palavra-chave estão na mensagem
                    if len(message_tokens) == 1:
                        if tokens[0] == message_tokens[0]:
                            result += 1
                    else:        
                        result += sum(1 for t in tokens if t in message_tokens)

                # Armazena a pontuação para cada intenção                        
                scores[intent] = result
            
            if any(scores.values()):
                print(scores)
                # Retorna a intent com mais correspondências
                best_intent = max(scores, key=scores.get)
                return best_intent
            return "default"

    def _extract_entities(self, message: str) -> Dict[str, List[str]]:
            """Extrai entidades usando regex."""
            entities = {"date": [], "hour": [], "material": [], "total": []}
            message_normalized = self.parse_message(message)           
           
            # Extração com regex
            for entity_name, config in self.entities.items():
                for pattern in config["patterns"]:
                    matches = re.finditer(pattern, message_normalized, re.IGNORECASE)
                    for match in matches:
                        value = match.group(0)
                        if value.startswith("met"):
                            value = "metalicas"
                        elif value.startswith("pla"):
                            value = "plasticas"
                        elif entity_name == "hour" and value.endswith("h"):
                            value = value.replace("h", "") 
                        entities[entity_name].append(value.strip())
            # Remover duplicatas
            for key in entities:
                entities[key] = list(set(entities[key]))
            return entities
    