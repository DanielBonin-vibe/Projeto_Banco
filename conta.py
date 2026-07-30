class Conta:
    id_conta = 10000

    def __init__(self, cpf_cliente, saldo, historico, numero_conta):
        self.cpf_cliente = cpf_cliente
        self.saldo = saldo
        self.historico =  historico
        self.numero_conta = numero_conta
        self.id_conta = Conta.id_conta

        Conta.id_conta += 1