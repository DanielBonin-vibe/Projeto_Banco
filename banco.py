from cliente import Cliente
from conta import Conta


class Banco:

##################################################
# Cliente
    def cadastrar_cliente(self, nome, idade, cpf, saldo):
        ...
    def remover_cliente(self): 
        ...
    def buscar_cliente(self, buscar_cpf):
        ...
    def listar_clientes(self):
        ...
##################################################
# Conta
        
    def consultar_saldo(self, cpf):
        ...

    def depositar(self, cpf, valor_deposito):
        ...
  
    def sacar(self, cpf, valor_saque):
        ...

    def transferir(self, chave_transferidor, chave_receptor, valor_transferido):
        ...
            

###################################################
# Menus

    def menu_principal(self):
        print('=' * 50)
        print('=' * 15, 'BANCO DO BONIN', '=' * 15)
        print('=' * 50)
        print()
        print('1 - Acessar área do servidor')
        print('2 - Acessar área do cliente' )
        return int(input('Informe a seleção desejada: '))
        
    def menu_servidor(self):
        print()
        print('=' * 50)
        print('=' * 15,'ÁREA DO SERVIDOR', '=' * 15)
        print('=' * 50)
        print()
        print('1 - Cadastrar cliente')
        print('2 - Buscar cliente')
        print('3 - Listar clientes')
        print('0 - Voltar')
        return input('Informe a ação requerida: ')
        

    def menu_cliente(self):
        print()
        print('=' * 50)
        print('=' * 15,'ÁREA DO CLIENTE', '=' * 15)
        print('=' * 50)
        print()
        print('1 - Consultar Saldo')
        print('2 - Realizar depósito')
        print('3 - Realizar saque')
        print('4 - Realizar transferência')
        print('0 - Voltar')
        return input('Digite a Ação requerida: ')
