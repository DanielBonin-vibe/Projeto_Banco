from repositories import conta_repository

def cadastro_conta_service(cpf_titular, saldo):

    if saldo < 0:
        raise ValueError('O saldo mínimo de arbertura é 0.0')

    resultado = conta_repository.cadastro_conta(cpf_titular, saldo)

    if resultado == 0:
        raise ValueError('Erro ao cadastrar a conta.')
    
    return resultado

def encerrar_conta_service(cpf):
    saldo = conta_repository.consultar_saldo(cpf)

    if saldo == 0:
        raise Exception('Não foi possível consultar a conta.')
        
    if saldo[0] < 0:
        raise ValueError('É necessário que o saldo seja igual a 0,00 para encerrar a conta.')

    if saldo is None:
        raise ValueError('Conta não encontrada.')

    resultado = conta_repository.encerrar_conta(cpf)

    if resultado == 0:
        raise Exception('Erro ao encerrar conta.')

    return resultado

def listar_contas_service():
    resultado = conta_repository.listar_contas()

    if resultado == 0:
        raise Exception('Não foi possível encontrar nenhuma conta para listar.')

    return resultado

def buscar_conta_service(cpf):

    if not cpf:
        raise ValueError('CPF inválido.')

    resultado = conta_repository.buscar_conta(cpf)

    if resultado == 0:
        raise Exception('Não foi possível buscar a conta.' )

    if resultado is None:
        raise ValueError('Conta não encontrada')

    return resultado

##############################################################

def consultar_saldo_service(cpf):
    resultado = conta_repository.consultar_saldo(cpf)

    if resultado == 0:
        raise ValueError('Não foi possível listar as contas.')

    return resultado

def deposito_saldo():
    ...

def saque_saldo():
    ...

def transferencia():
    ...