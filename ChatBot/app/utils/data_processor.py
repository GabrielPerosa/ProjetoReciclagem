from datetime import datetime
from app.utils.load_data import load_data

# os

class DataProcessor:
    def __init__(self):
        self.data = load_data("app/data/mock.json")
        #self.data = load_data(os.getenv("API_URL"))

    #def update_data(self):
    #    self.data = load_data(os.getenv("API_URL"))

    def get_material_per_hour(self, material: str, date: str, hour: str):
        """
        Retorna o total de um material em uma data e hora específica.
        """
        total = 0
        for h in self.data[material][date]:
            if h.startswith(hour):
                total += self.data[material][date][h]
        return total
    
    def get_material_per_date(self, material: str, date: str):
        """
        Retorna o total de um material em uma data específica.
        """
        total = 0
        for h in self.data[material][date]:
            total += self.get_material_per_hour(material, date, h)
        return total
    
    def get_all_material(self, material: str):
        """
        Retorna o total acumulado de um material em todas as datas.
        """
        total = 0
        for date in self.data[material]:
            total += self.get_material_per_date(material, date)
        return total
    
    def get_total_each_material_per_hour(self, date: str, hour: str):
        """
        Retorna o total de peças boas e refugadas em uma data e hora específicas.
        """
        total_good = 0 
        total_scrap = 0
    
        # Percorre todos os materiais e soma as quantidades
        for material in self.data["material"]:
            if material == "refugos":
                total_scrap += self.get_material_per_hour(material, date, hour)
                continue
            
            total_good += self.get_material_per_hour(material, date, hour)
            
        return round(total_good, 2), round(total_scrap, 2)
        
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
        return good_percent, scrap_percent, total_processed 

    def get_last_date(self):
        """
        Retorna a última data disponível nos dados.
        """   
        last_date = None
        for m in self.data["material"]:
            for string_date in self.data[m]:
                date = datetime.strptime(string_date, "%d/%m/%Y")
                if last_date is None or date > last_date:
                    last_date = date
        
        return last_date.strftime("%d/%m/%Y")
    
    def get_last_hour(self):
        """
        Retorna a última hora disponível na última data.
        """
        last_hour = None
        for material in self.data["material"]:
            for string_hour in self.data[material][self.get_last_date()]:
                hour = datetime.strptime(string_hour, "%H:%M")
                if last_hour is None or hour > last_hour:
                    last_hour = hour
        
        return last_hour.strftime("%H:%M")
    
