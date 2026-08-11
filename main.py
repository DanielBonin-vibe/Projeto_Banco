from banco import Banco

banco = Banco()

while True:
    opcao_inicial = banco.menu_principal()

    if opcao_inicial == 1:
        nome = input('Informe o seu nome completo:')
        idade = input('Informe sua idade de nascimento: ')
        cpf = input('Informe seu CPF(Sem pontuação): ')
        banco.cadastrar_cliente(nome, idade, cpf)

        cpf_titular = input('Informe o CPF do titular da conta(Sem pontuação: )')
        saldo = input('informe o saldo inicial a ser depositado: ')
        banco.abrir_conta(cpf_titular, saldo)

    elif opcao_inicial == 2:
        opcao_servidor = banco.menu_servidor()

        if opcao_servidor == 1:
            cpf_buscado = input('Informe o CPF do cliente: ')
            banco.buscar_cliente(cpf_buscado)
            
        elif opcao_servidor == 2:
            banco.listar_clientes()

    elif opcao_inicial == 3:
        opcao_cliente = banco.menu_cliente()

        if opcao_cliente == 1:
            cpf_buscado = input('Informe o CPF da conta: ')
            banco.consultar_saldo(cpf_buscado)
        elif opcao_cliente == 2:
            cpf_do_titular = input('Informe o CPF do titular da conta: ')
            deposito = input('Informe o valor do depósito')
            banco.depositar(cpf_do_titular, deposito)
        elif opcao_cliente == 3:
            cpf_do_titular = input('Informe o CPF do titular da conta: ')
            saque = input('Informe o valor do saque: ')
            banco.sacar(cpf_do_titular, saque)
        elif opcao_cliente == 4:
            ...
        elif opcao_cliente == 5:
            id_conta = int(input('Informe o ID da sua conta: '))
            banco.fechar_conta(id_conta)

        

        
