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
| TÍTULO DO CHAMADO:                            |       NÍVEL DE PRIORIDADE:                  |
|                                               |                                             |
|                                               |                                             |
|===============================================|=============================================|
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
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- TELEFONE

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
| TÍTULO DO CHAMADO:                            |       NÍVEL DE PRIORIDADE:                  |
|                                               |                                             |
|                                               |                                             |
|===============================================|=============================================|
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
        elif telefone == "x" or telefone == "X":
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

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- LOCAL


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
| TÍTULO DO CHAMADO:                            |       NÍVEL DE PRIORIDADE:                  |
|                                               |                                             |
|                                               |                                             |
|===============================================|=============================================|
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
        elif local == "x" or local == "X":
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

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- TITULO

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
| TÍTULO DO CHAMADO:                            |       NÍVEL DE PRIORIDADE:                  |
|                                               |                                             |
|                                               |                                             |
|===============================================|=============================================|
| DESCRIÇÃO DO CHAMADO:                                                                       |
|                                                                                             |
|                                                                                             |
|=====================================================================================|=======|
| CANCELAR OPERAÇÃO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   x   |
|_____________________________________________________________________________________|_______|""")
        titulo = input("\n Título do seu Chamado: ").title().strip() 
        if titulo == "":
            limpar_tela()
            continue
        elif titulo == "x" or titulo == "X":
            certeza = input("Precione 'X' Novamente para SAIR: ")
            if certeza == "x" or certeza == "X":
                limpar_tela()
                return
            else:
                limpar_tela()
                continue
        elif len(titulo) > 44:
            limpar_tela()
            print("Mensagem Muito Longa, favor escreva menos! ")
            continue
        else:
            break
    limpar_tela()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- PRIORIDADE

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
| TÍTULO DO CHAMADO:                            |       NÍVEL DE PRIORIDADE:                  |
|                                               |                                             |
| {str(titulo):<45} |                                             |
|===============================================|=============================================|
| DESCRIÇÃO DO CHAMADO:                                                                       |
|                                                                                             |
|                                                                                             |
|=====================================================================================|=======|
| CANCELAR OPERAÇÃO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |   x   |
|_____________________________________________________________________________________|_______|""")
        print_prioridades()
        prioridade_tipo = ""
        prioridade = input("\n Selecione o Nível de Prioridade: ").title().strip() 
        if prioridade == "":
            limpar_tela()
            continue
        elif prioridade == "x" or prioridade == "X":
            certeza = input("Precione 'X' Novamente para SAIR: ")
            if certeza == "x" or certeza == "X":
                limpar_tela()
                return
            else:
                limpar_tela()
                continue
        elif prioridade == "1":
            prioridade_tipo = "Sem Pressa"
            break
        elif prioridade == "2":
            prioridade_tipo = "Atencao Necessaria"
            break
        elif prioridade == "3":
            prioridade_tipo = "URGENCIA"
            break
        else:
            limpar_tela()
            print("Erro na Escolha, Tente novamente..")
            continue
    limpar_tela()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- DETALHES

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
| TÍTULO DO CHAMADO:                            |       NÍVEL DE PRIORIDADE:                  |
|                                               |                                             |
| {str(titulo):<45} | {str(prioridade + " " + prioridade_tipo):<43} |
|===============================================|=============================================|
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
        elif descricao == "x" or descricao == "X":
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
| TÍTULO DO CHAMADO:                            |       NÍVEL DE PRIORIDADE:                  |
|                                               |                                             |
| {str(titulo):<45} | {str(prioridade + " " + prioridade_tipo):<43} |
|===============================================|=============================================|
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
                "Titulo" : titulo,
                "Prioridade" : prioridade,
                "Prioridade_texto" : prioridade_tipo,
                "Descricao" : descricao,
                "Data e Momento" : tempo,
                "ID" : novo_id
            }
            salvar_chamados(novo_chamado)
            limpar_tela()
            print(f"Chamado enviado com sucesso!")
            return
        elif salvar.lower() == 'n':
            limpar_tela()
            print("Operação Cancelada! ")
            break
        else:
            limpar_tela()
            print("Erro na Digitação, tente novamente! ")
            continue
