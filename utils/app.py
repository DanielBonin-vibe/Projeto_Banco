from fastapi import FastAPI
from pydantic import BaseModel
from utils import banco_de_dados

app = FastAPI()

class Cliente(BaseModel):
    nome: str
    idade: int
    cpf: str

class Conta(BaseModel):
    cpf_titular: str
    saldo: int

#########################################################
# Cliente:

@app.post('/cliente')
def cadastrar_cliente_api(cliente: Cliente):
    
    banco_de_dados.cadastro_cliente(cliente)

    return cliente

@app.delete('/cliente/{id_cliente}')
def remover_cliente_api(id_cliente):

    banco_de_dados.remover_cadastro(id_cliente)

    return {'Mensagem': 'Usuário removido!'}

@app.get('/cliente')
def listar_clientes_api():

    listagem  = banco_de_dados.listar_clientes()

    return listagem 


#############################################################
# Contas: 

@app.post('/conta')
def abertura_conta_api(conta: Conta):

    banco_de_dados.abertura_conta(conta)

    return conta

@app.delete('/conta/{id_conta}')
def fechar_conta_api(id_conta):

    banco_de_dados.fechar_conta(id_conta)

    return {'Mensagem': 'Conta fechada, até uma próxima!'}

@app.get('/conta')
def consultar_conta_api():

    consulta = banco_de_dados.consultar_conta()

    return consulta

@app.get('/conta/{cpf_buscado}')
def buscar_cliente_e_conta_api(cpf_buscado):

    resultado = banco_de_dados.buscar_cliente_e_conta(cpf_buscado)

    return resultado

#################################################################
# Ações: 

@app.get('/conta/{cpf_buscado}')
def consulta_saldo_api(cpf_buscado):

    saldo = banco_de_dados.consultado_saldo(cpf_buscado)

    return saldo

@app.post('/conta/{cpf_do_titular}/{deposito}')
def deposito_saldo_api(cpf_do_titular, deposito):

    resultado = banco_de_dados.deposito_saldo(cpf_do_titular, deposito)

    return resultado

@app.post('conta/{cpf_do_titular}/{saque}')
def sacar_saldo_api(cpf_do_titular, saque):

    resultado = banco_de_dados.sacar_saldo(cpf_do_titular, saque)

    return resultado

@app.post('/conta/{cpf_titular_transferidor}/{cpf_titular_recebedor}/{transferencia}')
def transferencia_api(cpf_titular_transferidor, cpf_titular_recebedor, transferencia):

    resultado = banco_de_dados.transferencia(cpf_titular_transferidor, cpf_titular_recebedor, transferencia)

    return resultado