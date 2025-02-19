import json
DATAPATH = "database/dados.json"

def carregar_exercicios():
    try:
        with open(DATAPATH, "r") as file: 
            content = file.read().strip()
            if content:
                return json.loads(content)
            else:
                return {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Deu Erro Parceiro")
        return {}
