import random
import spacy
import unicodedata
from typing import Dict, List
import re
from app.services.load_data import LoadData 

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_md")
        self.intents = LoadData('app/data/intents.json')
        self.entities = LoadData('app/data/entities.json')
        self.responses = LoadData('app/data/responses.json')
        self.production_data = LoadData('http://localhost:8000/parts/')
        self.last_responses = {}
        self.context = {}

    def _detect_intent(self, message: str) -> str:
            """Detecta a intenção com base em palavras-chave definidas."""
            message = message.lower()
            message = unicodedata.normalize('NFKD', message).encode('ASCII', 'ignore').decode('utf-8')
            message = re.sub(r'[^\w\s]', '', message)
            message.strip()
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
            for entity_name, config in self.entities.items():
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
    def _format_response(self, intent: str, entities: Dict[str, List[str]]) -> str:
        """Formata a resposta com base na intenção e entidades."""
        responses = self.responses.get(intent, self.responses["default"])
        available = [r for r in responses if r != self.last_responses.get(intent)]
        response = random.choice(available or responses)
        self.last_responses[intent] = response

        print(entities)

        if "{material}" in response:
            if entities["material"]:
                material_str = ", ".join(entities["material"])
            else:
                material_str = ", ".join(self.production_data["material"])
            response = response.replace("{material}", material_str)

        # Substituir {quantidade} se presente na resposta
        if "{quantidade}" in response:
            if entities["material"]:
                material = entities["material"][0]
                if material in self.production_data["quantidade"]:
                    qty = self.production_data["quantidade"][material]
                else:
                    qty = "desconhecida"  # Valor padrão para material não encontrado
            else:
                qty = sum(self.production_data["quantidade"].values())
            response = response.replace("{quantidade}", str(qty))

        # Substituir {taxa} se presente na resposta
        if "{taxa}" in response:
            if entities["taxa"]:
                taxa_tipo = " ".join(entities["taxa"]).lower()
                if "acerto" in taxa_tipo:
                    taxa_valor = self.production_data["taxa"]["acerto"]
                elif "refugo" in taxa_tipo:
                    taxa_valor = self.production_data["taxa"]["refugo"]
                else:
                    taxa_valor = "desconhecida"
            else:
                taxa_valor = self.production_data["taxa"]["acerto"]  # Padrão
            response = response.replace("{taxa}", taxa_valor)

        return response
    def process_message(self, message: str) -> Dict[str, any]:
        intent = self._detect_intent(message)
        entities = self._extract_entities(message)
        response = self._format_response(intent, entities)

        self.context['last_intent'] = intent
        self.context['last_entities'] = entities
        self.context['last_response'] = response

        return {
            "intent": intent,
            "entities": entities,
            "response": response
        }