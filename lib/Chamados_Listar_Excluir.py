from lib.Limpar import limpar_tela
from lib.Chamados_Carregamento import *

def remover_chamados():
    while True:
        limpar_tela()
        chamados = carregar_chamados()

        if not isinstance(chamados, dict) or "chamados" not in chamados:
            print("Erro: O JSON está mal formatado ou corrompido.")
            return
        if not chamados["chamados"]:
            print("Adicione Novos Chamados Antes para usar essa Função!")
            return

        chamados_ordenados = sorted(
            (chamado for chamado in chamados["chamados"] if "Prioridade" in chamado),
            key=lambda x: int(x["Prioridade"])
        )
        print(".________________________________________________________________.")
        print("|                                                                |")
        print("|           -=- CHAMADOS EM ABERTO -=-                           |")
        print("|==============================|=====|===========================|")

        for chamado in chamados_ordenados:
            print(f"|  {chamado['Titulo']:<28}| {chamado['ID']:<3} | {chamado['Prioridade']} - {chamado['Prioridade_texto']:<21} |")

        print("|====================================|=====================|=====|")
        print("|                                    | VOLTAR . . . . . .  |  X  |")
        print("|____________________________________|_____________________|_____|")

        opcao = input("\nEscolha um chamado para remover pelo ID: ").strip().upper()

        if opcao == "X":
            limpar_tela()
            break

        chamado_selecionado = next((chamado for chamado in chamados["chamados"] if chamado.get("ID") == opcao), None)
        if chamado_selecionado:
            print(f"\nTem certeza que deseja remover o chamado '{chamado_selecionado['Titulo']}'? (S/N)")
            confirmacao = input().strip().upper()

        if confirmacao == "S":
            chamados["chamados"] = [chamado for chamado in chamados["chamados"] if chamado.get("ID") != opcao]
            chamados["chamados_encerrados"].append(chamado_selecionado)
            salvar_chamados_removidos(chamados)
            limpar_tela()
            print("\nChamado encerrado com sucesso!")

        else:
            print("\nID não encontrado. Tente novamente.")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def deletar_tudo():
    caminho_arquivo = "database/dados.json"  
    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write("{}") 

    print("Todos os chamados foram deletados! Mas a pergunta é, PORQUE????????? ")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def listar_chamados():
    inverter_prioridade = False 

    while True:
        limpar_tela()
        chamados = carregar_chamados()
        if not chamados:
            limpar_tela()
            print("Adicione Novos Chamados Antes para usar essa Função! ")
            return

        if inverter_prioridade:
            chamados_ordenados = sorted(chamados["chamados"], key=lambda x: int(x["Prioridade"]))
        else:
            chamados_ordenados = sorted(chamados["chamados"], key=lambda x: int(x["Prioridade"]), reverse=True)

        print(".________________________________________________________________.")
        print("|                                                                |")
        print("|           -=- CHAMADOS EM ABERTO -=-                           |")
        print("|==============================|=====|===========================|")

        for chamado in chamados_ordenados:
            print(f"|  {chamado['Titulo']:<28}| {chamado['ID']:<3} | {chamado['Prioridade']} - {chamado['Prioridade_texto']:<21} |")

        print("|==============================|=====|=====================|=====|")
        print("| INVERTER PRIORIDADES . . . . |  I  | VOLTAR . . . . . . .|  X  |")
        print("|______________________________|_____|_____________________|_____|")
        print("|                                                          |     |")
        print("| LIMPAR TUDO OQUE TEM NESSA LISTA PARA SEMPRE . . . . . . |  L  |")
        print("|__________________________________________________________|_____|")

        opcao = input("\nEscolha uma opção: ").strip().upper()

        if opcao == "I":
            inverter_prioridade = not inverter_prioridade 
        elif opcao == "X":
            limpar_tela()
            break
        elif opcao == "L":
            certeza01 = input("Tem Certeza? (S/N)").upper()
            if certeza01 == "S":
                certeza02 = input("TEM CERTEZA? (S/N)").upper()
                if certeza02 == "S":
                    limpar_tela()
                    deletar_tudo()
                    print("Acabou")
                    break
                else:
                    limpar_tela()
                    continue
            else:
                limpar_tela()
                continue
        else:
            print("Opção inválida! Tente novamente.")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def listar_chamados_finalizados():
    inverter_prioridade = False 

    limpar_tela()
    while True:
        chamados = carregar_chamados()

        chamados_encerrados = chamados.get("chamados_encerrados", [])
        if not isinstance(chamados_encerrados, list) or not chamados_encerrados:
            print("Tem nada aqui meu parceiro.")
            return

        chamados_validos = [
            chamado for chamado in chamados_encerrados
            if isinstance(chamado, dict) and "Prioridade" in chamado and chamado["Prioridade"] is not None
        ]

        if inverter_prioridade:
            chamados_ordenados = sorted(chamados_validos, key=lambda x: int(x.get("Prioridade", 0)))
        else:
            chamados_ordenados = sorted(chamados_validos, key=lambda x: int(x.get("Prioridade", 0)), reverse=True)

        print(".________________________________________________________________.")
        print("|                                                                |")
        print("|           -=- CHAMADOS FINALIZADOS -=-                         |")
        print("|==============================|=====|===========================|")

        for chamado in chamados_ordenados:
            titulo = chamado.get("Titulo", "Sem Título")
            chamado_id = chamado.get("ID", "N/A")
            prioridade = chamado.get("Prioridade", "N/A")
            prioridade_texto = chamado.get("Prioridade_texto", "N/A")
            print(f"|  {titulo:<28}| {chamado_id:<3} | {prioridade} - {prioridade_texto:<21} |")

        print("|                              |     |                           |")
        print("|==============================|=====|=====================|=====|")
        print("| INVERTER PRIORIDADES . . . . |  I  | VOLTAR . . . . . . .|  X  |")
        print("|______________________________|_____|_____________________|_____|")

        opcao = input("\n ").strip().upper()

        if opcao == "I":
            inverter_prioridade = not inverter_prioridade 
        elif opcao == "X":
            limpar_tela()
            break
        else:
            limpar_tela()
            print("Opção inválida! Tente novamente.")
