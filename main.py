from banco import Banco
from cliente import Cliente 
from conta import Conta

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
        ...

    elif opcao_inicial == 3:
        opcao_cliente = banco.menu_cliente()

        if opcao_cliente == 1:
            ...
        elif opcao_cliente == 2:
            ...
        elif opcao_cliente == 3:
            ...
        elif opcao_cliente == 4:
            ...
        elif opcao_cliente == 5:
            id_conta = int(input('Informe o ID da sua conta: '))
            banco.fechar_conta(id_conta)
        
