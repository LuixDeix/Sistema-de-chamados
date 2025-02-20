from lib.Limpar import limpar_tela
from lib.Chamados_Carregamento import *

def decisao_de_busca():
    limpar_tela()

    while True: 
        print(
        '''
.________________________________________.
|                                        |
|          -=- S.C.L.I.L.D -=-           |
|====================================|===|
| Buscar Chamados por ID . . . . . . | 1 |
| Buscar Chamados por Descrição. . . | 2 |
|                                    |   |
|====================================|===|
| Voltar . . . . . . . . . . . . . . | X |
|____________________________________|___|
        ''')
        escolha = input("Digite sua opção: ")
        if escolha == "1":
            buscar_chamados_id()

        elif escolha == "2":
            buscar_chamados_descricao()

        elif escolha == "x" or escolha == "X":
            limpar_tela()
            return

        else:
            limpar_tela()
            print("Erro na Opção Selecionada, Tente Novamente... ")
            continue

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def buscar_chamados_id():
    limpar_tela()
    chamados = carregar_chamados()
    if not chamados:
        limpar_tela()
        print("Adicione Novos Chamados Antes para usar essa Função! ")
        return
    
    print(".________________________________________________________________.")
    print("|                                                                |")
    print("|           -=- CHAMADOS EM ABERTO -=-                           |")
    print("|==============================|=====|===========================|")

    for chamado in chamados:
        prioridade = chamado['Prioridade']
        prioridade_texto = chamado['Prioridade_texto']

        print(f"|  {chamado['Titulo']:<28}| {chamado['ID']:<3} | {prioridade} - {prioridade_texto:<21} |")

    print("|==============================|=====|=====================|=====|")
    print("| INVERTER PRIORIDADES . . . . |  I  | VOLTAR . . . . . . .|  X  |")
    print("|______________________________|_____|_____________________|_____|")

    print("")
    
    try:
        opcao = input("Digite o ID do Chamado: ").strip()
        
        chamado_selecionado = next((chamado for chamado in chamados["chamados"] if chamado["ID"] == opcao), None)
        
        if chamado_selecionado:
            nome = chamado_selecionado["Nome"]
            telefone = chamado_selecionado["Telefone"]
            local = chamado_selecionado["Local"]
            titulo = chamado_selecionado["Titulo"]
            prioridade = chamado_selecionado["Prioridade"]
            prioridade_texto = chamado_selecionado["Prioridade_texto"]
            descricao = chamado_selecionado["Descricao"]
            id = chamado_selecionado["ID"]
        else:
            limpar_tela()
            print("Chamado não encontrado com o ID informado.")
            return
        
    except ValueError:
        print("Entrada inválida.")
        return
    limpar_tela()

    print(f"""
._____________________________________________________________________________________________.
|                                                                                             |
|                                 -=- CHAMADO {id} -=-                                         |
|=============================================================================================|
| NOME:                                         |       TELEFONE:        |      LOCAL:        |
|                                               |                        |                    |""")
    print(f"| {str(nome):<45} | {str(telefone):<22} | {str(local):<18} |")
    print(f"""|===============================================|========================|====================|
| TÍTULO DO CHAMADO:                            |       NÍVEL DE PRIORIDADE:                  |
|                                               |                                             |
| {str(titulo):<45} | {str(prioridade + " " + prioridade_texto):<43} |
|===============================================|=============================================|
| DESCRIÇÃO DO CHAMADO:                                                                       |
|                                                                                             |
| {str(descricao):<91} |
|=====================================================================================|=======|""")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def buscar_chamados_descricao():
    limpar_tela()
    chamados = carregar_chamados()

    if not chamados or not chamados.get("chamados", []):
        limpar_tela()
        print("Adicione Novos Chamados Antes para usar essa Função!")
        return

    termo_busca = input("Digite uma palavra ou frase para buscar na descrição: ").strip().lower()

    chamados_encontrados = [
        chamado for chamado in chamados["chamados"]
        if termo_busca in chamado["Descricao"].lower()
    ]

    limpar_tela()
    if not chamados_encontrados:
        print("Nenhum chamado encontrado com o termo informado.")
        return

    print(".________________________________________________________________.")
    print("|                                                                |")
    print("|           -=- CHAMADOS ENCONTRADOS -=-                         |")
    print("|==============================|=====|===========================|")

    for chamado in chamados_encontrados:
        prioridade = chamado['Prioridade']
        prioridade_texto = chamado['Prioridade_texto']

        print(f"|  {chamado['Titulo']:<28}| {chamado['ID']:<3} | {prioridade} - {prioridade_texto:<21} |")

    print("|==============================|=====|===========================|")
    print("|                                    | VOLTAR . . . . . . .|  X  |")
    print("|____________________________________|_____________________|_____|")

    while True:
        opcao = input("\nDigite o ID do chamado para ver detalhes ou 'X' para voltar: ").strip().upper()

        if opcao == "X":
            limpar_tela()
            return
        
        chamado_selecionado = next((chamado for chamado in chamados_encontrados if chamado["ID"] == opcao), None)

        if chamado_selecionado:
            limpar_tela()
            print(f"""
._____________________________________________________________________________________________.
|                                                                                             |
|                                 -=- CHAMADO {chamado_selecionado["ID"]} -=-                 |
|=============================================================================================|
| NOME:                                         |       TELEFONE:        |      LOCAL:        |
|                                               |                        |                    |""")
            print(f"| {chamado_selecionado['Nome']:<45} | {chamado_selecionado['Telefone']:<22} | {chamado_selecionado['Local']:<18} |")
            print(f"""|===============================================|========================|====================|
| TÍTULO DO CHAMADO:                            |       NÍVEL DE PRIORIDADE:                  |
|                                               |                                             |
| {chamado_selecionado['Titulo']:<45} | {chamado_selecionado['Prioridade']} - {chamado_selecionado['Prioridade_texto']:<43} |
|===============================================|=============================================|
| DESCRIÇÃO DO CHAMADO:                                                                       |
|                                                                                             |
| {chamado_selecionado['Descricao']:<91} |
|=====================================================================================|=======|""")
        else:
            print("ID não encontrado, tente novamente.")
