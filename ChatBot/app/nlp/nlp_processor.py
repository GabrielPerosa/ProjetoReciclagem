import random
from app.nlp.syntatic_analyser import SyntaticAnalyzer
from typing import Dict, List
from app.utils.load_data import load_data 
from app.utils.data_processor import DataProcessor

class NLPProcessor:
    def __init__(self):
        self.responses = load_data('app/data/responses.json')
        self.data_proc = DataProcessor()
        self.syntatic_analyser = SyntaticAnalyzer()
        self.last_responses = {}
        self.last_date = self.data_proc.get_last_date()
        self.last_hour = self.data_proc.get_last_hour()
        self.context = {}
        

    def _format_response(self, intent: str, entities: Dict[str, List[str]]) -> str:
        """Formata a resposta com base na intenção e entidades."""
        responses = self.responses.get(intent, self.responses["default"])
        available = [r for r in responses if r != self.last_responses.get(intent)]
        response = random.choice(available or responses)
        self.last_responses[intent] = response

        # Coletar entidades com fallback
        material = (entities.get("material") or [None])[0]
        date = (entities.get("date") or [None])[0]
        hour = (entities.get("hour") or [None])[0]

        # Formatar quantidade e detalhes com base na combinação de entidades
        if "{quantidade}" in response:
            if material:
                if date and hour:
                    qty = self.data_proc.get_material_per_hour(material, date, hour)
                    data_info = f"- {date}"
                    hour_info = f"no período de {hour} horas"
                elif hour:
                    qty = self.data_proc.get_material_per_hour(material, self.last_date, hour)
                    data_info = f"de {self.last_date} (último registro)"
                    hour_info = f"no período de {hour} horas"
                elif date:
                    qty = self.data_proc.get_material_per_date(material, date)
                    data_info = f"{date}"
                    hour_info = ""
                else:
                    qty = self.data_proc.get_material_per_hour(material, self.last_date, self.last_hour)
                    data_info = f"de {self.last_date} (último registro)"
                    hour_info = f"no intervalo de {self.last_hour} horas"
            elif date:
                if hour:
                    qty = self.data_proc.get_total_each_material_per_hour(date, hour)
                    data_info = f"- {date}"
                    hour_info = f"no período de {hour} horas"
                else:
                    qty = self.data_proc.get_total_each_material_per_hour(date)
                    data_info = f"{date}"
                    hour_info = ""
            elif hour:
                qty, _ = self.data_proc.get_total_each_material_per_hour(self.last_date, hour)
                data_info = f"de {self.last_date} (último registro)"
                hour_info = f"no período de {hour} horas"
            else:
                goods, scrap = self.data_proc.get_total_each_material_per_hour(self.last_date, self.last_hour)
                qty = goods + scrap
                material = ""  # Não menciona o tipo de material
                data_info = f"de {self.last_date} (último registro)"
                hour_info = f"no intervalo de {self.last_hour} horas"

            response = response.replace("{quantidade}", str(qty))
            response = response.replace("{material}", f"peças {material}" if material else "")
            response = response.replace("{data}", data_info)
            response = response.replace("{hora}", hour_info)
    
        # Substituir taxa (taxa_boa, taxa_ruim e total)
        if any(token in response for token in ["{taxa_boa}", "{taxa_ruim}", "{total}"]):
            good_percent, scrap_percent, total = self.data_proc.calc_percent_per_hour(self.last_date, self.last_hour)
            response = response.replace("{taxa_boa}", f"{good_percent:.2f}% peças boas")
            response = response.replace("{taxa_ruim}", f"{scrap_percent:.2f}% refugos")
            response = response.replace("{total}", str(total))

        return response
    
    def update_datetime(self):
        self.last_date = self.data_proc.get_last_date()
        self.last_hour = self.data_proc.get_last_hour()
        
    def process_message(self, message: str) -> Dict[str, any]:
        """Processa a mensagem, mantendo e atualizando o contexto."""
        self.update_datetime()
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