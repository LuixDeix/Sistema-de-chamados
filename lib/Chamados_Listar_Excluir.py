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

        opcao = input("\nEscolha uma opção: ").strip().upper()

        if opcao == "I":
            inverter_prioridade = not inverter_prioridade 
        elif opcao == "X":
            limpar_tela()
            break
        else:
            print("Opção inválida! Tente novamente.")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def listar_chamados_finalizados():
    inverter_prioridade = False 

    while True:
        limpar_tela()
        chamados = carregar_chamados()

        if not chamados or not chamados.get("chamados_encerrados"):
            limpar_tela()
            print("Não há chamados finalizados para exibir.")
            return

        if inverter_prioridade:
            chamados_ordenados = sorted(chamados["chamados_encerrados"], key=lambda x: int(x["Prioridade"]))
        else:
            chamados_ordenados = sorted(chamados["chamados_encerrados"], key=lambda x: int(x["Prioridade"]), reverse=True)

        print(".________________________________________________________________.")
        print("|                                                                |")
        print("|           -=- CHAMADOS FINALIZADOS -=-                         |")
        print("|==============================|=====|===========================|")

        for chamado in chamados_ordenados:
            print(f"|  {chamado['Titulo']:<28}| {chamado['ID']:<3} | {chamado['Prioridade']} - {chamado['Prioridade_texto']:<21} |")

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
            print("Opção inválida! Tente novamente.")
