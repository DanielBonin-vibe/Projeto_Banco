from banco import Banco
from utils import menus
from relatorios import validacao
banco = Banco()
while True:
    opcao_principal = menus.menu_principal()

    if opcao_principal == 1:
        while True:
            opcao_cliente = menus.menu_cliente()

            if opcao_cliente == 1:
                nome = input('Informe o seu nome completo: ')
                idade = input('Informe a sua idade: ')
                cpf = input('Informe o seu CPF:  ')
                banco.cadastro_cliente(nome, idade, cpf)

            elif opcao_cliente == 2:
                banco.listar_clientes()

            elif opcao_cliente == 3:
                

            elif opcao_cliente == 4:
                ...

            elif opcao_cliente == 0:
                break
                     
    elif opcao_principal == 2:
        while True:
            opcao_conta = menus.menu_conta()

            if opcao_conta == 1:
                ...

            elif opcao_conta == 2:
                ...

            elif opcao_conta == 3:
                ...

            elif opcao_conta == 4:
                ...

            elif opcao_conta == 5:
                ...

            elif opcao_conta == 0:
                break

    elif opcao_principal == 3:
        while True:
            opcao_operacoes = menus.menu_operacoes()

            if opcao_operacoes == 1:
                ...

            elif opcao_operacoes == 2:
                ...

            elif opcao_operacoes == 3:
                ...

            elif opcao_operacoes == 0:
                break
            
    elif opcao_principal == 4:
        while True:
            opcao_relatorio = menus.menu_relatorios()

            if opcao_relatorio == 1:
                while True:
                    opcao_relatorio_cliente = menus.menu_relatorios_clientes()

                    if opcao_relatorio_cliente == 1:
                        ...

                    elif opcao_relatorio_cliente == 2:
                        ...

                    elif opcao_relatorio_cliente == 3:
                        ...

                    elif opcao_relatorio_cliente == 4:
                        ...

                    elif opcao_relatorio_cliente == 0:
                        break

            if opcao_relatorio == 2:
                while True:
                    opcao_relatorio_conta = menus.menu_relatorios_contas()

                    if opcao_relatorio_conta == 1:
                        ...

                    elif opcao_relatorio_conta == 2:
                        ...

                    elif opcao_relatorio_conta == 3:
                        ...

                    elif opcao_relatorio_conta == 0:
                        break


            elif opcao_relatorio == 0:
                break

    elif opcao_principal == 0:
        print("Encerrando sistema...")
        break