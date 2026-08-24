from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from utils import banco_de_dados

app = FastAPI()

class Cliente(BaseModel):
    nome: str = Field(min_lenght=3)
    idade: int = Field(gt=0)
    cpf: str = Field(min_lenght=11, max_lenght=11, pattern=r"^\d{11}$")

class Conta(BaseModel):
    cpf_titular: str = Field(min_lenght=11, max_lenght=11, pattern=r"^\d{11}$")
    saldo: int 

#########################################################
# Cliente:

@app.post('/cliente')
def cadastrar_cliente_api(cliente: Cliente):
    
    banco_de_dados.cadastro_cliente(cliente)

    return cliente

@app.delete('/cliente/{id_cliente}', status_code=204)
def remover_cliente_api(id_cliente):

    quantidade = banco_de_dados.remover_cadastro(id_cliente)

    if quantidade == 0:
        raise HTTPException(
            status_code=404,
            detail='Usuário não encontrado.'
        )
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

@app.delete('/conta/{id_conta}', status_code=204)
def fechar_conta_api(id_conta):

    quantidade = banco_de_dados.fechar_conta(id_conta)

    if quantidade == 0:
        raise HTTPException(
            status_code=404,
            detail='Conta não encontrada.'
        )

@app.get('/conta', status_code=201)
def consultar_conta_api():

    consulta = banco_de_dados.consultar_conta()

    return consulta

@app.get('/conta/buscar/{cpf_buscado}', status_code=201)
def buscar_cliente_e_conta_api(cpf_buscado):

    resultado = banco_de_dados.buscar_cliente_e_conta(cpf_buscado)

    return resultado

#################################################################
# Ações: 

@app.get('/conta/consulta-saldo{cpf_buscado}')
def consulta_saldo_api(cpf_buscado):

    saldo = banco_de_dados.consultado_saldo(cpf_buscado)

    return saldo

@app.post('/conta/deposito-saldo{cpf_do_titular}/{deposito}')
def deposito_saldo_api(cpf_do_titular, deposito):

    resultado = banco_de_dados.deposito_saldo(cpf_do_titular, deposito)

    return resultado

@app.post('conta/{cpf_do_titular}/{saque}')
def sacar_saldo_api(cpf_do_titular, saque):

    resultado = banco_de_dados.sacar_saldo(cpf_do_titular, saque)

    return resultado

@app.post('/conta/transferencia/{cpf_titular_transferidor}/{cpf_titular_recebedor}/{transferencia}')
def transferencia_api(cpf_titular_transferidor, cpf_titular_recebedor, transferencia):
    try:
        resultado = banco_de_dados.transferencia(cpf_titular_transferidor, cpf_titular_recebedor, transferencia)
        return resultado
    except ValueError as erro:
        raise HTTPException(
            status_code=400,
            detail=str(erro)
        )