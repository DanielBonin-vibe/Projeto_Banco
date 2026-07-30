class Cliente:
    id_cliente = 1

    def __init__(self, nome, idade, cpf):
        self.id_cliente = Cliente.id_cliente
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

        Cliente.id_cliente += 1
