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
        total = (entities.get("total") or [None])[0]

        # Formatar quantidade e detalhes com base na combinação de entidades
        if "{quantidade}" in response:
            if material:
                if date and hour:
                    qty = self.data_proc.get_material_per_hour(material, date, hour)
                    data_info = f" - {date}"
                    hour_info = f" no horário de {hour} horas"
                elif hour:
                    qty = self.data_proc.get_material_per_hour(material, self.last_date, hour)
                    data_info = f" de {self.last_date} (último registro)"
                    hour_info = f" no período de {hour} horas"
                elif date:
                    qty = self.data_proc.get_material_per_date(material, date)
                    data_info = f" - {date}"
                    hour_info = ""
                elif total:
                    qty = self.data_proc.get_all_of_material(material)
                    data_info = ""
                    hour_info = ""
                else:
                    qty = self.data_proc.get_material_per_hour(material, self.last_date, self.last_hour)
                    data_info = f" de {self.last_date} (último registro)"
                    hour_info = f" no intervalo de {self.last_hour} horas"
            elif date:
                if hour:
                    qty, _ = self.data_proc.get_total_each_material_per_hour(date, hour)
                    data_info = f" do dia {date}"
                    hour_info = f" no período de {hour} horas"
                else:
                    materials = self.data_proc.data["material"]
                    qty = 0
                    for m in materials:
                        if m != "descarte":
                            qty += self.data_proc.get_material_per_date(m, date)
                   
                    data_info = f" no dia {date}"
                    hour_info = ""
            elif hour:
                qty, _ = self.data_proc.get_total_each_material_per_hour(self.last_date, hour)
                data_info = f" da data {self.last_date} (último registro)"
                hour_info = f" no período de {hour} horas"
            else:
                goods, scrap = self.data_proc.get_total_each_material_per_hour(self.last_date, self.last_hour)
                qty = goods + scrap
                material = ""  # Não menciona o tipo de material
                data_info = f" do dia {self.last_date} (último registro)"
                hour_info = f" no intervalo de {self.last_hour} horas"

            response = response.replace("{quantidade}", f"{str(qty)} ")
            response = response.replace("{material}", f"{material}" if material else "")
            response = response.replace("{data}", data_info)
            response = response.replace("{hora}", hour_info)
    
        # Substituir taxa (taxa_boa, taxa_ruim e total)
        if any(token in response for token in ["{taxa_boa}", "{taxa_ruim}", "{total}"]):
            
            d = (date or self.last_date)
            h = (hour or self.last_hour)
            
            result = self.data_proc.calc_percent_per_hour(d, h)
            if result == None:
                return "Não há registro na base de dados para o período especificado" 
            else:
                good_percent = result[0]
                scrap_percent = result[1]
                total = result[2]
                response = response.replace("{taxa_boa}", f"{good_percent:.2f}% peças boas")
                response = response.replace("{taxa_ruim}", f"{scrap_percent:.2f}% refugos")
                response = response.replace("{total}", str(total))
        return response
    
    # Atualiza os ultimos registros de dados da classe NLP
    def update_datetime(self):
        self.last_date = self.data_proc.get_last_date()
        self.last_hour = self.data_proc.get_last_hour()
        
    def process_message(self, message: str) -> Dict[str, any]:
        """Processa a mensagem, mantendo e atualizando o contexto."""
        try:
            self.update_datetime()
            self.data_proc.update_data()
            intent = self.syntatic_analyser._detect_intent(message)
            entities_detected = self.syntatic_analyser._extract_entities(message)

            # Se a intenção mudou, limpar as entidades do contexto
            response = self._format_response(intent, entities_detected)
        except Exception as e:
            intent = []
            entities_detected = []
            response = "Erro ao processar prompt {}".format(e)
            
        return {
            "response": response
        }