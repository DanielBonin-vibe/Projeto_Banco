from cliente import Cliente

class Banco:
    def __init__(self):
        self.lista_clientes = []
        self.lista_contas = []

##################################################
# Cliente
    def cadastrar_cliente(self, nome, idade, cpf):

        for cliente in self.lista_clientes:

            if cliente.cpf == cpf:
                print('Não podemos cadastrar o mesmo cliente duas vezes')
                break

        else:
            cliente = Cliente(nome, idade, cpf)
            self.lista_clientes.append(cliente)
            print('Cliente cadastrado na nossa base de dados')

# Vamos por aqui uam função para criar uma conat vinculado a novo cliente automaticamente.


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
    def criar_conta(self, nome):

    def consultar_saldo(self):

    def depositar(self):

    def sacar(self):

    def transferir(self):

###################################################
# Menus

    def menu_principal(self):
        print('=' * 50)
        print('=' * 20, 'BANCO DO BONIN', '=' * 20)
        print('=' * 50)
        print()
        print('1 - Acessar área do servidor')
        print('2 - Acessar área do cliente' )
        return int(input('Informe a seleção desejada: '))
        
    def menu_servidor(self):
        print()
        print('=' * 50)
        print('=' * 20,'ÁREA DO SERVIDOR', '=' * 20)
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
        print('=' * 20,'ÁREA DO SERVIDOR', '=' * 20)
        print('=' * 50)
        print()
        print('1 - Criar conta')
        print('2 - Consultar cliente')
        print('3 - Listar clientes')
        print('0 - Voltar')
        return input('Digite a Ação requerida: ')
