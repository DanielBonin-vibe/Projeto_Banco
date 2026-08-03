from banco import Banco
from cliente import Cliente 
from conta import Conta

banco = Banco()

while True:
    opcao_inicial = banco.menu_principal()

    if opcao_inicial == 1:
        opcao_servidor = banco.menu_servidor()

    elif opcao_inicial == 2:
        opcao_cliente = banco.menu_cliente()

# Cadastrar Cliente:
        if opcao_servidor == '1':
            nome = input('Digite o nome completo do cliente: ')
            idade = int(input('Digite a idade do cliente'))
            cpf = int(input('Digite o CPF do cliente(Apenas número): '))
            saldo = float('Informe o saldo a ser transferido inicialmente: ')
            banco.cadastrar_cliente(nome, idade, cpf, saldo)


        # Buscar Cliente:
        elif opcao_servidor == '2':
            cpf_buscar = input('Informe o cpf do cliente a ser procurado: ')
            banco.buscar_cliente(cpf_buscar)


        # Listar Clientes
        elif opcao_servidor == '3':
            banco.listar_clientes()


    # Consultar Saldo
    if opcao_cliente == '1':
        banco.consultar_saldo()

    # Depositar
    elif opcao_cliente == '2':
        valor_depósito = input('Informe o valor de depósito: ')

    # Sacar
    opcao_cliente == '3':

    # Transferir
    opcao_cliente == '4':



