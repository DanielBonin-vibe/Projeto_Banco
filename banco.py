from cliente import Cliente
from conta import Conta
from utils import banco_de_dados


class Banco:

##################################################
# Cliente
    def cadastrar_cliente(self, nome, idade, cpf):
        banco_de_dados.cadastro_cliente(nome, idade, cpf)
        print('Cliente cadastrado, siga com a abertura da conta...')
    def remover_cliente(self, id_cliente): 
        banco_de_dados.remover_cadastro(id_cliente)

    def buscar_cliente(self, cpf_buscado):
        banco_de_dados.buscar_cliente_e_conta(cpf_buscado)
        
    def listar_clientes(self):
        banco_de_dados.listar_clientes()


##################################################
# Conta

    def abrir_conta(self, cpf_titular, saldo):
        banco_de_dados.abertura_conta(cpf_titular, saldo)
        print('Conta criada e vinculada!')
    def fechar_conta(self, id_conta):
        banco_de_dados.fechar_conta(id_conta)
        print('Conta encerrada, esperamos encontrar-lo novamente!')

##################################################
# Ações
        
    def consultar_saldo(self, cpf_buscado):
        banco_de_dados.consulta_saldo(cpf_buscado)
        print('Ação concluída')

    def depositar(self, cpf_do_titular, deposito):
        banco_de_dados.deposito_saldo(cpf_do_titular, deposito)
        print('Depósito concluído.')
  
    def sacar(self, cpf_do_titular, saque):
        banco_de_dados.sacar_saldo(cpf_do_titular, saque)
        print('Saque concluído.')

    def transferir(self,cpf_titular_transferidor, cpf_titular_recebedor, transferencia):
        banco_de_dados.transferencia(cpf_titular_transferidor, cpf_titular_recebedor, transferencia)
        print('Transferência concluída.')

###################################################
# Menus

    def menu_principal(self):
        print('=' * 50)
        print('=' * 15, 'BANCO DO BONIN', '=' * 15)
        print('=' * 50)
        print()
        print('1 - Desejo ser cliente')
        print('2 - Acessar área do servidor')
        print('3 - Acessar área do cliente' )
        return int(input('Informe a seleção desejada: '))
        
    def menu_servidor(self):
        print()
        print('=' * 50)
        print('=' * 15,'ÁREA DO SERVIDOR', '=' * 15)
        print('=' * 50)
        print()
        print('1 - Buscar cliente')
        print('2 - Listar clientes')
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
        print('5 - Fechar conta corrente.')
        print('0 - Voltar')
        return input('Digite a Ação requerida: ')


        



