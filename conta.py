class Conta:
    id_conta = 10000

    def __init__(self, cpf_titular, saldo_inicial):
        self.cpf_cliente = cpf_titular
        self.saldo = saldo_inicial
        self.id_conta = Conta.id_conta

        Conta.id_conta += 1