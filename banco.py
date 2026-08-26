from utils import banco_de_dados
from services import cliente_service, conta_service

class Banco:

    def cadastro_cliente(self, nome, idade, cpf):
        cliente_service.cadastro_cliente_service(nome, idade, cpf)
        print('Cliente cadastrado, siga com a abertura da conta...')

    def remover_cadastro(self, cpf): 
        cliente_service.remover_cadastro_service(cpf)

    def listar_clientes(self):
        cliente_service.listar_clientes_service()

##################################################
# Conta

    def cadastro_conta(self, cpf_titular, saldo):
        conta_service.cadastro_conta_service(cpf_titular, saldo)
       
    def encerrar_conta(self, cpf):
        conta_service.encerrar_conta_service(cpf)
        

##################################################
# Ações
        
    def consultar_saldo(self, cpf):
        banco_de_dados.consulta_saldo(cpf)
        print('Ação concluída')

    def depositar(self, cpf_titular, deposito):
        banco_de_dados.deposito_saldo(cpf_titular, deposito)
        print('Depósito concluído.')
  
    def sacar(self, cpf_titular, saque):
        banco_de_dados.sacar_saldo(cpf_titular, saque)
        print('Saque concluído.')

    def transferir(self,cpf_titular_transferidor, cpf_titular_recebedor, transferencia):
        banco_de_dados.transferencia(cpf_titular_transferidor, cpf_titular_recebedor, transferencia)
        print('Transferência concluída.')