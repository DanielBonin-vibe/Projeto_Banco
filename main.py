from services import cliente_service, conta_service
from repositories import relatorios_repository
from utils import menus
from relatorios import validacao
from decimal import Decimal
while True:
    opcao_principal = menus.menu_principal()

    if opcao_principal == 1:
        while True:
            opcao_cliente = menus.menu_cliente()

            if opcao_cliente == 1:
                nome = input('Informe o seu nome completo: ')
                idade = input('Informe a sua idade: ')
                cpf = input('Informe o seu CPF:  ')
                cliente_service.cadastro_cliente_service(nome, idade, cpf)

            elif opcao_cliente == 2:
                cliente_service.listar_clientes_service()

            elif opcao_cliente == 3:
                cpf_atual = ('Informe o atual CPF do seu perfil: ')
                nome = input('Informe o seu novo nome completo: ')
                idade = input('Informe a sua nova idade: ')
                cpf = input('Informe o seu novo CPF:  ')
                cliente_service.atualizar_cadastro_service(cpf_atual, nome, idade, cpf)

            elif opcao_cliente == 4:
                cpf = input('Informe o CPF do cliente a ser removido: ')
                cliente_service.remover_cadastro_service(cpf)

            elif opcao_cliente == 0:
                break
                     
    elif opcao_principal == 2:
        while True:
            opcao_conta = menus.menu_conta()

            if opcao_conta == 1:
                cpf_titular = input('Informe o CPF do cliente que será o titular da conta: ')
                saldo = Decimal(input('Informe o saldo inicial: '))
                conta_service.cadastro_conta_service(cpf_titular, saldo)

            elif opcao_conta == 2:
                cpf = input('Informe o CPF a ser buscado: ')
                conta_service.buscar_conta_service(cpf)

            elif opcao_conta == 3:
                conta_service.listar_contas_service()

            elif opcao_conta == 4:
                cpf = input('Informe o CPF da conta a ser consultada: ')
                conta_service.buscar_conta_service(cpf)

            elif opcao_conta == 5:
                cpf = input('infome o CPF da conta a ser encerrada: ')
                conta_service.encerrar_conta_service(cpf)

            elif opcao_conta == 0:
                break

    elif opcao_principal == 3:
        while True:
            opcao_operacoes = menus.menu_operacoes()

            if opcao_operacoes == 1:
                cpf = input('Informe o CPF da conta: ')
                deposito = Decimal(input('Informe o valor do depósito: '))
                conta_service.deposito_saldo_service(cpf, deposito)

            elif opcao_operacoes == 2:
                cpf = input('Informe o CPF da conta: ')
                saque = Decimal(input('Informe o valor do saque: '))
                conta_service.saque_saldo_service(cpf, saque)

            elif opcao_operacoes == 3:
                cpf_transferidor = input('Informe o CPF do transferidor: ')
                cpf_recebedor = input('Informe o CPF do reebedor; ')
                transferencia = Decimal(input('Informe o valor a ser transferido: '))
                conta_service.transferencia_service(cpf_transferidor, cpf_recebedor, transferencia)

            elif opcao_operacoes == 0:
                break
            
    elif opcao_principal == 4:

        if validacao.senha():
            while True:
                opcao_relatorio = menus.menu_relatorios()

                if opcao_relatorio == 1:
                    while True:
                        opcao_relatorio_cliente = menus.menu_relatorios_clientes()

                        if opcao_relatorio_cliente == 1:
                            resultado = relatorios_repository.relatorio_geral_cliente()
                            print(resultado)

                        elif opcao_relatorio_cliente == 2:
                            resultado = relatorios_repository.relatorio_ordem_alfabetica()
                            print(resultado)
                        elif opcao_relatorio_cliente == 3:
                            resultado = relatorios_repository.relatorio_cpf()
                            print(resultado)
                        elif opcao_relatorio_cliente == 4:
                            resultado = relatorios_repository.relatorio_faixa_etaria()
                            print(resultado)

                        elif opcao_relatorio_cliente == 0:
                            break

                elif opcao_relatorio == 2:
                    while True:
                        opcao_relatorio_conta = menus.menu_relatorios_contas()

                        if opcao_relatorio_conta == 1:
                            resultado = relatorios_repository.relatorio_geral_conta()
                            print(resultado)

                        elif opcao_relatorio_conta == 2:
                            resultado = relatorios_repository.relatorio_saldo()
                            print(resultado)

                        elif opcao_relatorio_conta == 3:
                            resultado = relatorios_repository.relatorio_nivel_conta()
                            print(resultado)

                        elif opcao_relatorio_conta == 0:
                            break


                elif opcao_relatorio == 0:
                    break

    elif opcao_principal == 0:
        print("Encerrando sistema...")
        break