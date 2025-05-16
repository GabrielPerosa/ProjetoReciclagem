import requests
import json

def load_data(path: str):

    if path.startswith("http://") or path.startswith("https://"):
        return None
        response = requests.get(path)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            return Exception("Erro ao obter dados da URL")    
    else:
        if path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return Exception("Erro no nome do arquivo ou URL inválida")