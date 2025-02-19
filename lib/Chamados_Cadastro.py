from datetime import datetime
from lib.Limpar import limpar_tela
from lib.Chamados_Carregamento import *

hoje = datetime.now()
# print(hoje.strftime("%d-%m-%Y %H:%M"))

def cadastrar_chamados():
    chamados = carregar_chamados()
    limpar_tela()
    while True:
        print("""
._____________________________________________________________________________________________.
|                                                                                             |
|                                 -=- NOVO CHAMADO -=-                                        |
|=============================================================================================|
| NOME:                                         |       TELEFONE:        |      LOCAL:        |
|                                               |                        |                    |
|                                               |                        |                    |
|===============================================|========================|====================|
| DESCRIÇÃO DO CHAMADO:                                                                       |
|                                                                                             |
|                                                                                             |
|=====================================================================================|=======|
| CANCELAR OPERAÇÃO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   x   |
|_____________________________________________________________________________________|_______|""")
        
        nome = input("\n Digite seu nome: ").title().strip() 
        if nome == "":
            limpar_tela()
            continue
        elif nome == "x" or nome == "X":
            certeza = input("Precione 'X' Novamente para SAIR: ")
            if certeza == "x" or certeza == "X":
                limpar_tela()
                return
            else:
                limpar_tela()
                continue
        elif len(nome) > 43:
            limpar_tela()
            print("Mensagem Muito Longa, favor escreva menos! ")
            continue
        else:
            break
    limpar_tela()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    limpar_tela()
    while True:
        print("""
._____________________________________________________________________________________________.
|                                                                                             |
|                                 -=- NOVO CHAMADO -=-                                        |
|=============================================================================================|
| NOME:                                         |       TELEFONE:        |      LOCAL:        |
|                                               |                        |                    |""")
        print(f"| {str(nome):<45} |                        |                    |")
        print("""|===============================================|========================|====================|
| DESCRIÇÃO DO CHAMADO:                                                                       |
|                                                                                             |
|                                                                                             |
|=====================================================================================|=======|
| CANCELAR OPERAÇÃO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   x   |
|_____________________________________________________________________________________|_______|""")
        telefone = input("\n Digite seu Telefone de Contado: ").title().strip() 
        if telefone == "":
            limpar_tela()
            continue
        elif nome == "x" or nome == "X":
            certeza = input("Precione 'X' Novamente para SAIR: ")
            if certeza == "x" or certeza == "X":
                limpar_tela()
                return
            else:
                limpar_tela()
                continue
        elif len(telefone) > 20:
            limpar_tela()
            print("Mensagem Muito Longa, favor escreva menos! ")
            continue
        else:
            break
    limpar_tela()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


    while True:
        limpar_tela()
        print("""
._____________________________________________________________________________________________.
|                                                                                             |
|                                 -=- NOVO CHAMADO -=-                                        |
|=============================================================================================|
| NOME:                                         |       TELEFONE:        |      LOCAL:        |
|                                               |                        |                    |""")
        print(f"| {str(nome):<45} | {str(telefone):<22} |                    |")
        print("""|===============================================|========================|====================|
| DESCRIÇÃO DO CHAMADO:                                                                       |
|                                                                                             |
|                                                                                             |
|=====================================================================================|=======|
| CANCELAR OPERAÇÃO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   x   |
|_____________________________________________________________________________________|_______|""")
        local = input("\n Onde se localiza o caso: ").title().strip() 
        if local == "":
            limpar_tela()
            continue
        elif nome == "x" or nome == "X":
            certeza = input("Precione 'X' Novamente para SAIR: ")
            if certeza == "x" or certeza == "X":
                limpar_tela()
                return
            else:
                limpar_tela()
                continue
        elif len(local) > 16:
            limpar_tela()
            print("Mensagem Muito Longa, favor escreva menos! ")
            continue
        else:
            break
    limpar_tela()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    limpar_tela()
    while True:
        print("""
._____________________________________________________________________________________________.
|                                                                                             |
|                                 -=- NOVO CHAMADO -=-                                        |
|=============================================================================================|
| NOME:                                         |       TELEFONE:        |      LOCAL:        |
|                                               |                        |                    |""")
        print(f"| {str(nome):<45} | {str(telefone):<22} | {str(local):<18} |")
        print("""|===============================================|========================|====================|
| DESCRIÇÃO DO CHAMADO:                                                                       |
|                                                                                             |
|                                                                                             |
|=====================================================================================|=======|
| CANCELAR OPERAÇÃO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   x   |
|_____________________________________________________________________________________|_______|""")
        descricao = input("\n Descreva seu Chamado: ").title().strip() 
        if descricao == "":
            limpar_tela()
            continue
        elif nome == "x" or nome == "X":
            certeza = input("Precione 'X' Novamente para SAIR: ")
            if certeza == "x" or certeza == "X":
                limpar_tela()
                return
            else:
                limpar_tela()
                continue
        elif len(descricao) > 90:
            limpar_tela()
            print("Mensagem Muito Longa, favor escreva menos! ")
            continue
        else:
            break
    limpar_tela()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    limpar_tela()
    while True:
        print("""
._____________________________________________________________________________________________.
|                                                                                             |
|                                 -=- NOVO CHAMADO -=-                                        |
|=============================================================================================|
| NOME:                                         |       TELEFONE:        |      LOCAL:        |
|                                               |                        |                    |""")
        print(f"| {str(nome):<45} | {str(telefone):<22} | {str(local):<18} |")
        print(f"""|===============================================|========================|====================|
| DESCRIÇÃO DO CHAMADO:                                                                       |
|                                                                                             |
| {str(descricao):<91} |
|=====================================================================================|=======|
| CANCELAR OPERAÇÃO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   x   |
|_____________________________________________________________________________________|_______|""")
        salvar = input("\n Deseja realmente salvar esse Chamado? (S/N): ").title().strip() 
        if salvar == "":
            limpar_tela()
            continue
        elif salvar == "x" or salvar == "X":
            certeza = input("Precione 'X' Novamente para SAIR: ")
            if certeza == "x" or certeza == "X":
                limpar_tela()
                return
            else:
                limpar_tela()
                continue
        if salvar.lower() == 's':
            tempo = hoje.strftime("%d-%m-%Y %H:%M")

            dados = carregar_chamados()
            ids_existentes = [int(chamado["ID"]) for chamado in dados["chamados"]] if dados["chamados"] else []
            novo_id = str(max(ids_existentes) + 1).zfill(3) if ids_existentes else "001"

            novo_chamado = {
                "Nome": nome,
                "Telefone": telefone,
                "Local" : local,
                "Descricao" : descricao,
                "Data e Momento" : tempo,
                "ID" : novo_id
            }
            salvar_chamados(novo_chamado)
            limpar_tela()
            print(f"Chamado enviado com sucesso!")
            return
        elif salvar.lower() == 'n':
            limpar_tela
            print("Operação Cancelada! ")
            break
        else:
            limpar_tela()
            print("Erro na Digitação, tente novamente! ")
            continue
