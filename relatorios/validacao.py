from utils import menus, banco_de_dados

# Senha:

def senha():
    password = 'B@nin180506'
    count = 0

    while True:
        tentativa = input('Informe a senha do sistema: ')

        if tentativa == password:
            print('Acesso autorizado!')
            return True
            
        else:
            count += 1
            print('Senha incorreta!')

            if count == 3:
                print('Limite atingido')
                return False

############################################################

while True:
    opcao_relatorio = menus.menu_relatorios()

    if opcao_relatorio == 1:
        opcao_relatorio_clientes = menus.menu_relatorios_clientes()

        if opcao_relatorio_clientes == 1:
            banco_de_dados.relatorio_padrao_cliente()

        elif opcao_relatorio_clientes == 2:
            banco_de_dados.relatorio_nome_ordem_alfabetica_cliente()

        elif opcao_relatorio_clientes == 3:
            banco_de_dados.relatorio_cpf_cliente()

        elif opcao_relatorio_clientes == 4:
            banco_de_dados.relatorio_faixa_etaria_cliente()


    elif opcao_relatorio == 2:
        opcao_relatorio_contas = menus.menu_relatorios_contas()

        if opcao_relatorio_contas == 1:
            banco_de_dados.relatorio_padrao_conta()

        elif opcao_relatorio_contas == 2:
            banco_de_dados.relatorio_decrescente_saldo()

        elif opcao_relatorio_contas == 3:
            banco_de_dados.relatorio

        elif opcao_relatorio_contas == 4:
            ...

        elif opcao_relatorio_contas == 5:
            ...

    else:
        break