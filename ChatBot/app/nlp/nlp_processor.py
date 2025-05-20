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
        self.last_date = self.data_proc.get_last_date()
        self.last_hour = self.data_proc.get_last_hour()
        

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
            else:
                response = response.replace("{material}", "")
        # Substituir {quantidade}
        if "{quantidade}" in response:
            if entities["material"] and entities["hour"]:
                material = entities["material"][0]
                hour = entities["hour"][0]
                qty = self.data_proc.get_material_per_hour(material, self.last_date, hour)
                response = response.replace("{quantidade}", str(qty))
            if entities["material"] and entities["date"]:
                material = entities["material"][0]
                date = entities["date"][0]
                qty = self.data_proc.get_material_per_date(material, date)
                response = response.replace("{quantidade}", str(qty))
            else:
                goods, scrap = self.data_proc.get_total_each_material_per_hour(self.last_date, self.last_hour)
                response = response.replace("{quantidade}", str(goods+scrap))

        # Substituir {taxa}
        if "{total}" in response:
            print(self.last_date, self.last_hour)
            good_percent, scrap_percent, total = self.data_proc.calc_percent_per_hour(self.last_date, self.last_hour)
            response = response.replace("{taxa_boa}", f"{good_percent:.2f}% peças boas") 
            response = response.replace("{taxa_ruim}", f"{scrap_percent:.2f}% refugos")
            if "{total}" in response:
                response = response.replace("{total}", str(total))
        
        if "{hour}" in response: 
            if entities["hour"]:
                response = response.replace("{hour}", entities["hour"][0])
            else:
                response = response.replace("{hour}", self.last_hour)

        if "{date}" in response:
            if entities["date"]:
                response = response.replace("{date}", entities["date"][0])
            else:
                response = response.replace("{date}", self.last_date)
        return response

    def update_datetime(self):
        self.last_date = self.data_proc.get_last_date()
        self.last_hour = self.data_proc.get_last_hour()
        
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