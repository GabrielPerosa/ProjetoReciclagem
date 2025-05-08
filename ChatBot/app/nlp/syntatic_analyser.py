import re
from typing import Dict, List

class SyntaticAnalyzer:
    def _detect_intent(self, message: str) -> str:
            """Detecta a intenção com base em palavras-chave."""
            message = message.lower()
            for intent, keywords in self.intents.items():
                if any(keyword in message for keyword in keywords):
                    return intent
            return "default"

    def _extract_entities(self, message: str) -> Dict[str, List[str]]:
            """Extrai entidades usando regex e spaCy."""
            entities = {"codigo": [], "quantidade": [], "material": [], "taxa": []}

            # Processamento com spaCy
            doc = self.nlp(message)

            # Extração com regex
            for entity_name, config in self.entities_patterns.items():
                for pattern in config["patterns"]:
                    matches = re.finditer(pattern, message.lower(), re.IGNORECASE)
                    for match in matches:
                        if config["grupo"] is not None:
                            value = match.group(config["grupo"])
                        else:
                            value = match.group(0)
                        entities[entity_name].append(value)

            # Extração adicional com spaCy (ex.: números e materiais não capturados por regex)
            for token in doc:
                if token.like_num and "quantidade" not in entities or not entities["quantidade"]:
                    entities["quantidade"].append(token.text)
                if token.text.lower() in ["metálicas", "plásticas", "refugos"] and token.text.lower() not in entities["material"]:
                    entities["material"].append(token.text.lower())

            # Remover duplicatas
            for key in entities:
                entities[key] = list(set(entities[key]))

            return entities