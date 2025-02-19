import json
import os
DATAPATH = "database/dados.json"

def carregar_chamados():
    try:
        with open(DATAPATH, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if content:
                return json.loads(content)
            else:
                return {"chamados": []} 
    except FileNotFoundError:
        return {"chamados": []}
    except json.JSONDecodeError:
        print("Erro ao carregar o JSON!")
        return {"chamados": []}

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def salvar_chamados(novo_chamado):
    if not os.path.exists("database"):
        os.makedirs("database")

    dados = carregar_chamados()
    dados["chamados"].append(novo_chamado)

    with open(DATAPATH, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)