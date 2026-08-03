from cliente import Cliente
from conta import Conta
from json_utils import salvar_json

class Banco:
    def __init__(self):
        self.lista_clientes = []
        self.lista_contas = []

##################################################
# Cliente
    def cadastrar_cliente(self, nome, idade, cpf, saldo):

        for cliente in self.lista_clientes:
            if cliente.cpf == cpf:
                return 'Não podemos cadastrar o mesmo cliente duas vezes'
                

        else:
            cliente = Cliente(nome, idade, cpf)
            self.lista_clientes.append(cliente)

            lista_clientes = [] # Criamos uma lista nova para armazenar o append

            for cliente in self.lista_clientes:
                lista_clientes.append(cliente.to_dict()) # Adicione na nova lista 'lista_cleinte.append' a def 'to_dict'

            salvar_json('dados/clientes.json', lista_clientes)  # 'salvar_json' é a função, sendo 'dados/clientes.json' == salve ass info. dentro do arquivo 'cleintes.json', que está na pasta 'dados' e lista_clientes armazena os dict's

            print('Cliente cadastrado na nossa base de dados')

            conta = Conta(cpf, saldo)
            self.lista_contas.append(conta)
            print('Conta vinculada!')


    def buscar_cliente(self, buscar_cpf):
        for cliente in self.lista_clientes:

            if cliente.cpf == buscar_cpf:
                print('Cliente encontrado: ')
                print(cliente)
                break

            else: 
                print('Cliente não foi encontrado.')

            

    def listar_clientes(self):
        for cliente in self.lista_clientes:
            print(cliente)

##################################################
# Conta
        

    def consultar_saldo(self, cpf):
        for conta in self.lista_contas:
            if conta.cpf == cpf:
                return conta.saldo

            else: 
                return 'Este CPF não está vinculado a nenhuma conta'


    def depositar(self, cpf, valor_deposito):
        for conta in self.lista_contas:
            if conta.cpf == cpf:
                if valor_deposito >= 0:
                    conta.saldo += valor_deposito
                else: 
                    return 'Não é possível depositar um valor menor que ou igual a 0'
            else: 
                return 'Não encontramos nenhuma conta vinculada ao CPF informado.'
        return 'Depósito realizado com sucesso!'

            
    def sacar(self, cpf, valor_saque):
        for conta in self.lista_contas:
            if conta.cpf == cpf:
                if valor_saque >= conta.saldo:
                    conta.saldo -= valor_saque
                    return ('Realizando saque...')

                else: 
                    return 'Não podemos sacar um valor maior que o saldo!'
            else:
                return 'Não encontramos nenhuma conta vinculada ao CPF informado.'
        return ('Saque realizado com sucesso!')



    def transferir(self, chave_transferidor, chave_receptor, valor_transferido):
        for conta in self.lista_contas:
            if chave_transferidor == conta.id_conta:

                if valor_transferido > conta.saldo:
                    return 'Não é possível transferir um valor maior que o saldo!'
                
                conta.saldo -= valor_transferido
                print('Valor debitado')
                break
        else:
            return 'Não encontramos nenhuma conta vinculada a esta chave.'
    
        for conta in self.lista_contas:
            if chave_receptor == conta.id_conta:
                conta.saldo += valor_transferido
                return 'Transferência realizada com sucesso!'

        return 'Não encontramos nenhuma conta vinculada a esta chave.'
            


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
