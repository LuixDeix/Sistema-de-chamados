from lib.Limpar import limpar_tela
from lib.Chamados_Carregamento import *

def remover_chamados():
    pass

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
