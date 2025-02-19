from lib.Limpar import limpar_tela

def decisao_de_busca():
    limpar_tela()

    while True: 
        print(
        '''
|-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-|
|          -=- S.C.L.I.L.D -=-           |
|-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-|-=-|
| Buscar Chamados por ID . . . . . . | 1 |
| Buscar Chamados por Descrição. . . | 2 |
|                                    |   |
|-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-|-=-|
| Voltar . . . . . . . . . . . . . . | X |
|-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-|-=-|
        ''')
        escolha = input("Digite sua opção: ")
        if escolha == "1":
            limpar_tela()

        elif escolha == "2":
            limpar_tela()

        elif escolha == "x" or escolha == "X":
            limpar_tela()
            return

        else:
            limpar_tela()
            print("Erro na Opção Selecionada, Tente Novamente... ")
            continue

def buscar_chamados_id():
    pass

def buscar_chamados_descrição():
    pass
