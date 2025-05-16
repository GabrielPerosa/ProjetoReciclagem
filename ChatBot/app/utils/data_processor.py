from app.services.load_data import load_data
# os

class DataProcessor:
    def __init__(self):
        self.data = load_data("app/data/mock.json")
        #self.data = load_data(os.getenv("API_URL"))
    def get_material_per_hour(self, material: str, date: str, hour: str):
        total = 0
        for h in self.data[material][date]:
            if h.startswith(hour):
                total += self.data[material][date][h]
        return total
    
    def get_material_per_date(self, material: str, date: str):
        total = 0
        for h in self.data[material][date]:
            total += self.get_material_per_hour(material, date, h)
        return total
    
    def get_all_material(self, material: str):
        total = 0
        for date in self.data[material]:
            total += self.get_material_per_date(material, date)
        return total
    
    def get_total_each_material_per_hour(self, date: str, hour: str):
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
    
        # Obtendo soma de peças por hora 
        total_good, total_scrap = self.get_total_each_material_per_hour(date, hour)
        total_processed = total_good + total_scrap
    
        # Calculando percentuais
        scrap_percent = total_scrap * 100 / total_processed
        good_percent = total_good * 100 / total_processed
        
        return good_percent, scrap_percent, total_processed 
