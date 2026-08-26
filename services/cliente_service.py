from repositories import cliente_repository
def cadastro_cliente_service(nome, idade, cpf):

    if not nome: 
        raise ValueError('Nome inválido.')

    if idade < 18:
        raise ValueError('O cliente deve ser maior de 18 anos.')

    if not cpf:
        raise ValueError('CPF inválido.')

    resultado = cliente_repository.cadastro_cliente(nome, idade, cpf)

    if resultado == 0:
        raise Exception('Não foi possível cadastrar o cliente.')

    return resultado

def remover_cadastro_service(cpf):

    if not cpf:
        raise ValueError('CPF inválido.')

    resultado = cliente_repository.remover_cadastro(cpf)

    if resultado == 0:
        raise Exception ('Não possível remover o cliente.')

    return resultado

def listar_clientes_service():

    resultado = cliente_repository.listar_clientes()

    if resultado == 0:
        raise Exception('Não foi possível listar os clientes.')

    return resultado 