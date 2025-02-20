from lib.Chamados_Busca import *
from lib.Chamados_Cadastro import *
from lib.Chamados_Listar_Excluir import *
from lib.Chamados_Busca import *
from lib.Limpar import *

limpar_tela()
def escolhas():
    while True:
        print(
        '''
.________________________________________.
|                                        |
|          -=- S.C.L.I.L.D -=-           |
|====================================|===|
| Cadastrar novos chamados . . . . . | 1 |
| Buscar Chamados p/ Descrição/ID. . | 2 |
| Listar Chamados  . . . . . . . . . | 3 |
| Finalizar Chamado  . . . . . . . . | 4 |
| Chamados Finalizados . . . . . . . | 5 |
|                                    |   |
|====================================|===|
| Sair . . . . . . . . . . . . . . . | X |
|____________________________________|___|
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