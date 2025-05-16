import random
from app.nlp.syntatic_analyser import SyntaticAnalyzer
from typing import Dict, List
from app.services.load_data import load_data 
from app.utils.data_processor import DataProcessor

class NLPProcessor:
    def __init__(self):
        self.responses = load_data('app/data/responses.json')
        self.data_proc = DataProcessor()
        self.syntatic_analyser = SyntaticAnalyzer()
        self.last_responses = {}
        self.context = {}

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
                response = response.replace("{material}", material_str)

        # Substituir {quantidade}
        if "{quantidade}" in response:
            if entities["material"]:
                material = entities["material"][0]
                qty = self.data_proc.get_all_material(material)
            else:
                
                qty = sum(self.data_proc.get_all_material("quantidade"))
            response = response.replace("{quantidade}", str(qty))

        # Substituir {taxa}
        if "{taxa}" in response:
            if entities["taxa"]:
                taxa_tipo = " ".join(entities["taxa"]).lower()
                if "acerto" in taxa_tipo:
                    taxa_valor = self.data_proc["taxa"]["acerto"]
                elif "refugo" in taxa_tipo:
                    taxa_valor = self.data_proc["taxa"]["refugo"]
                else:
                    taxa_valor = "desconhecida"
            else:
                taxa_valor = self.data_proc["taxa"]["acerto"]  # Padrão
            response = response.replace("{taxa}", taxa_valor)

        return response

    def process_message(self, message: str) -> Dict[str, any]:
        """Processa a mensagem, mantendo e atualizando o contexto."""
        intent = self.syntatic_analyser._detect_intent(message)
        entities_detected = self.syntatic_analyser._extract_entities(message)

        # Se a intenção mudou, limpar as entidades do contexto
        response = self._format_response(intent, entities_detected)

        # Atualizar o contexto
        self.context['last_intent'] = intent
        self.context['last_response'] = response

        return {
            "intent": intent,
            "entities": entities_detected,
            "response": response
        }