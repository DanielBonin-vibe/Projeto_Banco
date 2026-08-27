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

def deposito_saldo_service(cpf, deposito):

    if deposito <= 0:
        raise Exception('Não é possível depositar valores menores ou igual a 0.')

    resultado = conta_repository.deposito_saldo(cpf, deposito)

    if resultado == 0:
        raise Exception('Não foi possivel localizar a conta.')

    return resultado

def saque_saldo(cpf, saque):

    if saque <= 0 :
        raise ValueError('Não é possível sacar valores menos ou iguais a 0.')

    saldo = conta_repository.consultar_saldo(cpf)

    if saldo is None:
        raise ValueError('Conta não encontrada.')

    if saque > saldo:
        raise ValueError('Não é possível sacar um valor maior que o saldo.')

    resultado = conta_repository.saque_saldo(cpf, saque)

    if resultado == 0:
        raise Exception('Não foi possível realizar o saque.')

    return resultado
    
def transferencia(cpf_transferidor, cpf_recebedor, transferencia):

    if cpf_transferidor == cpf_recebedor:
        raise ValueError('Erro, CPF(s) iguais.')

    if transferencia <= 0:
        raise ValueError('O valor da trasnferência deve ser maior que 0.')

    saldo = conta_repository.consultar_saldo(cpf_transferidor)

    if saldo is None:
        raise ValueError('Conta não encontrada.')

    if saldo < transferencia:
        raise ValueError('Não é possível enviar um valor maior que o saldo.')

    resultado = conta_repository.transferencia(cpf_transferidor, cpf_recebedor, transferencia)

    if resultado == 0:
        raise Exception('Não foi possível realizar a trasnferência.')
    
    return resultado