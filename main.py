from banco import Banco
from utils import menus
from relatorios import validacao

banco = Banco()

print("1 - INICIO DO MAIN")

banco = Banco()

print("2 - BANCO CRIADO")

while True:
    print("ANTES DO MENU PRINCIPAL")

    opcao_inicial = menus.menu_principal()

    print("OPÇÃO ESCOLHIDA:", opcao_inicial)

    if opcao_inicial == 1:

        nome = input('Informe o seu nome completo: ')
        idade = input('Informe sua idade de nascimento: ')
        cpf = input('Informe seu CPF: ')
        banco.cadastrar_cliente(nome, idade, cpf)

        cpf_titular = input('Informe o CPF do titular da conta: ')
        saldo = input('informe o saldo inicial a ser depositado: ')
        banco.abrir_conta(cpf_titular, saldo)

    elif opcao_inicial == 2:
        opcao_servidor = menus.menu_servidor()

        if opcao_servidor == 1:
            cpf_buscado = input('Informe o CPF do cliente: ')
            banco.buscar_cliente(cpf_buscado)
            
        elif opcao_servidor == 2:
            banco.listar_clientes()

        else:
            break   

    elif opcao_inicial == 3:
        opcao_cliente = menus.menu_cliente()

        if opcao_cliente == 1:
            cpf_buscado = input('Informe o CPF da conta: ')
            banco.consultar_saldo(cpf_buscado)
        elif opcao_cliente == 2:
            cpf_do_titular = input('Informe o CPF do titular da conta: ')
            deposito = input('Informe o valor do depósito: ')
            banco.depositar(cpf_do_titular, deposito)
        elif opcao_cliente == 3:
            cpf_do_titular = input('Informe o CPF do titular da conta: ')
            saque = input('Informe o valor do saque: ')
            banco.sacar(cpf_do_titular, saque)
        elif opcao_cliente == 4:
            cpf_titular_transferidor = input('Informe o CPF do titular da conta a realizar a transferência: ')
            cpf_titular_recebedor = input('Inform o CPF do titular da conta a receber a transferência: ')
            transferencia = input('Informe o valor da transferência: ')
            banco.transferir(cpf_titular_transferidor, cpf_titular_recebedor, transferencia)
        elif opcao_cliente == 5:
            id_conta = int(input('Informe o ID da sua conta: '))
            banco.fechar_conta(id_conta)

        else:
            break

    elif opcao_inicial == 4:
        acesso = validacao.senha()

        if acesso:
            validacao.relatorios()
        else:
            break
            

        
