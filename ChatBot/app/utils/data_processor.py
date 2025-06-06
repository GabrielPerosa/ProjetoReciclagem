from datetime import datetime
from app.utils.load_data import load_data
import os

class DataProcessor:
    def __init__(self):    
        try:
            self.data = load_data(os.getenv("API_URL"))
            self.environment = "production"
        except Exception as e: 
            self.data = load_data("app/data/mock.json")
            self.environment = "mock"

    def itemExists(self, material: str, date: str, hour: str):
        """
        Verifica se um material existe em uma data e hora específicas.
        """

        if material not in self.data:
            # Verifica se o material existe
            return False
        if date != None and date not in self.data[material]:
            # Verifica se a data existe para o material
            return False
        if hour != None:
            # Verifica se a hora existe para a data
            for h in self.data[material][date]:
                if h.startswith(hour):
                    return True
            return False

    def update_data(self):
        """Atualiza os dados carregando novamente do arquivo ou API."""
        if self.environment == "production":
            self.data = load_data(os.getenv("API_URL"))

    def get_material_per_hour(self, material: str, date: str, hour: str):
        """
        Retorna o total de um material em uma data e hora específica.
        """
        total = 0
        if self.itemExists(material, date, hour) == False:
            return 0
        for h in self.data[material][date]:
            if h.startswith(hour):
                total += self.data[material][date][h]
        return total 

    def get_material_per_date(self, material: str, date: str):
        """
        Retorna o total de um material em uma data específica.
        """
        total = 0
        if self.itemExists(material, date, None) == False:
            return 0
        for h in self.data[material][date]:
            total += self.get_material_per_hour(material, date, h)
        return total
    
    def get_all_of_material(self, material: str):
        """
        Retorna o total acumulado de um material em todas as datas.
        """
        total = 0
        for date in self.data[material]:
            total += self.get_material_per_date(material, date)
        return total
    def get_total_of_production(self):
        """
        Obtem o total da produção
        """
        total = 0
        for material in self.data["material"]:
            if material != "descarte":
                total += self.get_all_of_material(material)
        return total
    def get_total_per_date(self, date: str):
        """
        Retorna o total de peças boas e refugadas em uma data.
        """
        total_good = 0 
        total_scrap = 0
    
        # Percorre todos os materiais e soma as quantidades
        for material in self.data["material"]:
            if self.itemExists(material, date, None) == False:
                continue

            if material == "descarte":
                total_scrap += self.get_material_per_date(material, date)
                continue
            
            total_good += self.get_material_per_date(material, date)
            
        return total_good, total_scrap
    def get_total_each_material_per_hour(self, date: str, hour: str):
        """
        Retorna o total de peças boas e refugadas em uma data e hora específicas.
        """
        total_good = 0 
        total_scrap = 0

        # Percorre todos os materiais e soma as quantidades
        for material in self.data["material"]:
            if self.itemExists(material, date, hour) == False:
                continue
            if material == "descarte":
                total_scrap += self.get_material_per_hour(material, date, hour)
                continue
            total_good += self.get_material_per_hour(material, date, hour)            
        return total_good, total_scrap
        
    def calc_percent_per_hour(self, date: str, hour: str):
        """
        Calcula o percentual de boas e refugos em uma data e hora específicas.
        """
        # Obtendo soma de peças por hora 
        total_good, total_scrap = self.get_total_each_material_per_hour(date, hour)
        total_processed = total_good + total_scrap
        # Calculando percentuais
        try:
            scrap_percent = total_scrap * 100 / total_processed
            good_percent = total_good * 100 / total_processed
        except: 
            return None
        return round(good_percent, 2), round(scrap_percent, 2), total_processed 
    def calc_percent_per_date(self, date):
        """
        Calcula a porcentagem por data.
        """
        total_good, total_scrap = self.get_total_per_date(date)
        total_processed = total_good + total_scrap
        # Calculando percentuais
        try:
            scrap_percent = total_scrap * 100 / total_processed
            good_percent = total_good * 100 / total_processed
        except: 
            return None
        return round(good_percent, 2), round(scrap_percent, 2), total_processed 
        
    def calc_percent_total (self):
        """
        Calcula a porcentagem total da produção.
        """
        total_good = self.get_total_of_production()
        total_scrap = self.get_all_of_material("descarte")
        total_processed = total_good + total_scrap
        # Calculando percentuais
        try:
            scrap_percent = total_scrap * 100 / total_processed
            good_percent = total_good * 100 / total_processed
        except: 
            return None
        return round(good_percent, 2), round(scrap_percent, 2), total_processed 
        
    def get_last_date_of_material(self, material):
        """
        Retorna a última data disponível para o material.
        """   
        last_date = None
        for string_date in self.data[material]:
            date = datetime.strptime(string_date, "%d/%m/%Y")
            if last_date is None or date > last_date:
                last_date = date
        
        return last_date.strftime("%d/%m/%Y")
    
    def get_last_hour_of_material(self, material):
        """
        Retorna a última hora disponível na última data do material.
        """
        last_hour = None
        last_date = self.get_last_date_of_material(material)
        for string_hour in self.data[material][last_date]:
            # Percorre as horas da última data
            hour = datetime.strptime(string_hour, "%H:%M")
            if last_hour is None or hour > last_hour:
                    last_hour = hour
        return last_hour.strftime("%H:%M")
    
    def get_last_log_of_material(self, material):
        """
        Retorna a última data e hora de um material específico.
        """
        last_date = self.get_last_date_of_material(material)
        last_hour = self.get_last_hour_of_material(material)
        return last_hour, last_date
    
    def get_last_log(self):
        """
        Retorna a última data e hora de todos os materiais.
        """
        last_date = None
        last_hour = None
        for material in self.data["material"]: 
            
            hour, date=self.get_last_log_of_material(material)
            if last_hour is None or hour > last_hour or date > last_date:
                last_date = date
                last_hour = hour
        return last_hour, last_date