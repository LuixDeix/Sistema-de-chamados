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

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def salvar_chamados_removidos(chamados):
    estrutura_corrigida = {
        "chamados": chamados.get("chamados", []),  
        "chamados_encerrados": chamados.get("chamados_encerrados", [])
    }
    with open(DATAPATH, "w", encoding="utf-8") as f:
        json.dump(estrutura_corrigida, f, indent=4, ensure_ascii=False)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def print_prioridades():
    print("""
.___________________________________.
|                                   |
|            Prioridade             |
|===============================|===|
| Sem Pressa . . . . . . . . . .| 1 |
| Atenção Necessária . . . . . .| 2 |
| URGENTE  . . . . . . . . . . .| 3 |
|_______________________________|___|""")