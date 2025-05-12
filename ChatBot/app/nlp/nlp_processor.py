import random
import spacy
import unicodedata
from typing import Dict, List
import re
import os
from app.services.load_data import LoadData 

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_md")
        self.intents = LoadData('app/data/intents.json')
        self.entities = LoadData('app/data/entities.json')
        self.responses = LoadData('app/data/responses.json')
        self.production_data = LoadData(os.getenv('API_URL'))
        self.last_responses = {}
        self.context = {}
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

            if any(keyword in message_clean.split() for keyword in self.continuation_keywords):
                if 'last_intent' in self.context and self.context['last_intent'] != "default":
                    print(f"Continuação detectada, mantendo intenção: {self.context['last_intent']}")
                    return self.context['last_intent']
            
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
    ## 
    def _format_response(self, intent: str, entities: Dict[str, List[str]]) -> str:
        """Formata a resposta com base na intenção e entidades."""
        responses = self.responses.get(intent, self.responses["default"])
        available = [r for r in responses if r != self.last_responses.get(intent)]
        response = random.choice(available or responses)
        self.last_responses[intent] = response

        # Substituir {material}
        if "{material}" in response:
            if entities["material"]:
                material_str = ", ".join(entities["material"])
            else:
                material_str = ", ".join(self.production_data["material"])
            response = response.replace("{material}", material_str)

        # Substituir {quantidade}
        if "{quantidade}" in response:
            if entities["material"]:
                material = entities["material"][0]
                qty = self.production_data["quantidade"].get(material, "desconhecida")
            else:
                qty = sum(self.production_data["quantidade"].values())
            response = response.replace("{quantidade}", str(qty))

        # Substituir {taxa}
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
        """Processa a mensagem, mantendo e atualizando o contexto."""
        intent = self._detect_intent(message)
        entities_detected = self._extract_entities(message)

        # Se a intenção mudou, limpar as entidades do contexto
        if 'last_intent' in self.context and self.context['last_intent'] != intent:
            self.context['entities'] = {}
        
        # Inicializar entidades no contexto se ainda não existir
        if 'entities' not in self.context:
            self.context['entities'] = {"codigo": [], "quantidade": [], "material": [], "taxa": []}

        # Atualizar entidades detectadas no contexto
        for entity, values in entities_detected.items():
            if values:  # Só atualiza se houver novos valores
                self.context['entities'][entity] = values

        # Usar entidades do contexto para formatar a resposta
        entities_for_response = self.context['entities']
        response = self._format_response(intent, entities_for_response)

        # Atualizar o contexto
        self.context['last_intent'] = intent
        self.context['last_response'] = response

        return {
            "intent": intent,
            "entities": entities_for_response,
            "response": response
        }