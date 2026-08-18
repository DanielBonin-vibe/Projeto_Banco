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