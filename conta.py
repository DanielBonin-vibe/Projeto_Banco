class Conta:
    id_conta = 10000

    def __init__(self, cpf_titular, saldo_inicial):
        self.cpf_titular = cpf_titular
        self.saldo_inicial = saldo_inicial
        self.id_conta = Conta.id_conta

        Conta.id_conta += 1

    def to_dict(self):
        return {
            'cpf_titular': self.cpf_titular,
            'saldo_inicial': self.saldo_inicial, 
            'id_conta': self.id_conta
        }