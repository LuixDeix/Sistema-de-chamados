from lib.Chamados_Busca import *
from lib.Chamados_Cadastro import *
from lib.Chamados_Listar_Excluir import *
from lib.Chamados_Busca import *
from lib.Limpar import *

limpar_tela()

def calcular_dados_gerais():
    chamados = carregar_chamados()

    if not chamados:
        total_abertos = 0
        total_fechados = 0
    else:
        total_abertos = len(chamados.get("chamados", []))
        total_fechados = len(chamados.get("chamados_encerrados", []))

    total_chamados = total_abertos + total_fechados
    if total_chamados > 0:
        porcentagem_abertos = (total_abertos / total_chamados) * 100
        porcentagem_fechados = (total_fechados / total_chamados) * 100
    else:
        porcentagem_abertos = 0
        porcentagem_fechados = 0

    return total_abertos, total_fechados, round(porcentagem_abertos), round(porcentagem_fechados)

def escolhas():
    while True:
        total_abertos, total_fechados, porcentagem_abertos, porcentagem_fechados = calcular_dados_gerais()
        print(
        f'''
.________________________________________.  .______________________________.
|                                        |  |                              |
|          -=- S.C.L.I.L.D -=-           |  |     -=-  DADOS GERAIS  -=-   |
|====================================|===|  |======================|=======|
| Cadastrar novos chamados . . . . . | 1 |  |                      |       |
| Buscar Chamados p/ Descrição/ID. . | 2 |  | Chamados Abertos . . |  {total_abertos:<3}  |
| Listar Chamados  . . . . . . . . . | 3 |  |    Porcentagem       |  {porcentagem_abertos}%  |
| Finalizar Chamado  . . . . . . . . | 4 |  |______________________|_______|
| Chamados Finalizados . . . . . . . | 5 |  |                      |       |
|                                    |   |  | Chamados Fechados  . |  {total_fechados:<3}  |
|====================================|===|  |    Porcentagem       |  {porcentagem_fechados}%  |
| Sair . . . . . . . . . . . . . . . | X |  |______________________|_______|
|____________________________________|___|  |______________________|_______|
        ''' 
        )

        decisao = input("Digite sua opção: ")
        if decisao == "1":
            cadastrar_chamados()

        elif decisao == "2":
            decisao_de_busca()

        elif decisao == "3":
            listar_chamados()   

        elif decisao == "4":
            remover_chamados()

        elif decisao == "5":
            listar_chamados_finalizados()

        elif decisao == "x" or decisao == "X":
            limpar_tela()
            print()
            print("Até Mais! ;D ")
            print()
            break

        else:
            limpar_tela()
            print("Erro na Opção Selecionada, Tente Novamente... ")
            continue

escolhas()