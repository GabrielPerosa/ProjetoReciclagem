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
        self.last_date = None
        self.last_hour = None
        

    def select_response(self, intent: str) -> str:
        """Seleciona uma resposta aleatória com base na intenção."""
        responses = self.responses.get(intent, self.responses["default"])
        available = [r for r in responses if r != self.last_responses.get(intent)]
        response = random.choice(available or responses)
        self.last_responses[intent] = response
        
        return response
    def _format_response(self, intent: str, entities: Dict[str, List[str]]) -> str:
        """Formata a resposta com base na intenção e entidades."""

        response = self.select_response(intent)

        # Coletar entidades com fallback
        material = (entities.get("material") or [None])[0]
        date = (entities.get("date") or [None])[0]
        hour = (entities.get("hour") or [None])[0]
        total = (entities.get("total") or [None])[0]
        qty = 0
        # Formatar quantidade e detalhes com base na combinação de entidades
        if "{quantidade}" in response:
            if material:
                # Data e hora fornecidas
                if date and hour:
                    qty = self.data_proc.get_material_per_hour(material, date, hour)
                    data_info = f" - {date}"
                    hour_info = f" no horário de {hour} horas"
                # Hora fornecidas
                elif hour:
                    last_date = self.get_last_date(material)
                    qty = self.data_proc.get_material_per_hour(material, last_date, hour)
                    data_info = f" de {last_date} (último registro)"
                    hour_info = f" no período de {hour} horas"
                # Data fornecida
                elif date:
                    qty = self.data_proc.get_material_per_date(material, date)
                    data_info = f" - {date}"
                    hour_info = ""
                # Total requisitado
                elif total:
                    qty = self.data_proc.get_all_of_material(material)
                    data_info = ""
                    hour_info = ""
                else:
                    # Último registro do material
                    last_hour, last_date = self.data_proc.get_last_log_of_material(material)
                    qty = self.data_proc.get_material_per_hour(material, last_date, last_hour)
                    data_info = f" de {last_date} (último registro)"
                    hour_info = f" no intervalo de {last_hour} horas"
            # Não forneceu material, mas forneceu data
            elif date:
                # Data e hora fornecidas
                if hour:
                    qty, _ = self.data_proc.get_total_each_material_per_hour(date, hour)
                    data_info = f" do dia {date}"
                    hour_info = f" no período de {hour} horas"
                # Apenas data fornecida
                else:
                    goods, scraps = self.data_proc.get_total_per_date(date)
                    qty = goods + scraps
                    data_info = f" no dia {date}"
                    hour_info = ""
            # Apenas hora fornecida
            elif hour:
                goods, scraps = self.data_proc.get_total_each_material_per_hour(self.last_date, hour)
                qty = goods + scraps
                data_info = f" da data {self.last_date} (último registro)"
                hour_info = f" no período de {hour} horas"
            
            # Total requisitado
            elif total:
                qty = self.data_proc.get_total_of_production()
                material = "" 
                data_info = f" do dia {self.last_date} (último registro)"
                hour_info = f" no intervalo de {self.last_hour} horas"

            if qty == 0 and intent == "consultar_quantidade":
                return self.select_response("ausencia_de_dados")
            else:
                # Substituir quantidade, material, data e hora na resposta
                response = response.replace("{quantidade}", f"{str(qty)} ")
                response = response.replace("{material}", f"{material}" if material else "")
                response = response.replace("{data}", data_info)
                response = response.replace("{hora}", hour_info)
    
        # Substituir taxa (taxa_boa, taxa_ruim e total)
        if any(token in response for token in ["{taxa_boa}", "{taxa_ruim}", "{total}"]):
            
            d = (date or self.last_date)
            h = (hour or self.last_hour)
            if total:
                result = self.data_proc.calc_percent_total() 
            elif date:
                result = self.data_proc.calc_percent_per_date(date)
            else:
                result = self.data_proc.calc_percent_per_hour(d,h)
            
            if result == None:
                return self.select_response("ausencia_de_dados") 
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
        hour, date = self.data_proc.get_last_log()
        self.last_hour = hour
        self.last_date = date

    def process_message(self, message: str) -> Dict[str, any]:
        """Processa a mensagem, mantendo e atualizando o contexto."""
        try:
            self.update_datetime()
            self.data_proc.update_data()

            intent = self.syntatic_analyser._detect_intent(message)
            entities_detected = self.syntatic_analyser._extract_entities(message)
            response = self._format_response(intent, entities_detected)
        except Exception as e:    
            response = "Erro ao processar prompt: {}".format(e)
            
        return {
            "response": response
        }