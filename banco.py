from cliente import Cliente
from conta import Conta
from utils import banco_de_dados


class Banco:

##################################################
# Cliente
    def cadastrar_cliente(self, nome, idade, cpf):
        banco_de_dados.cadastro_cliente(nome, idade, cpf)
        print('Cliente cadastrado, siga com a abertura da conta')
    def remover_cliente(self, id_cliente): 
        banco_de_dados.remover_cadastro(id_cliente)

    def buscar_cliente(self, buscar_cpf):
        ...
    def listar_clientes(self):
        ...


##################################################
# Conta

    def abrir_conta(self, cpf_titular, saldo_inicial):

    def fechar_conta(self, id_conta)
##################################################
# Ações
        
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

    def menu_desejo_ser_cliente(self):
        print('=' * 50)
        print('=' * 15,'ÁREA DE CADASTRO', '=' * 15)
        print('=' * 50)
        return self.tornar_se_cliente()

    def tornar_se_cliente(self):
        nome = input('Digite o nome completo do cliente: ')
        idade = int(input('Digite a idade do cliente: '))
        cpf = int(input('Digite o CPF do cliente(Apenas número): '))

        return nome, idade, cpf
        



