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

@app.post('/cliente')
def cadastrar_cliente_api(cliente: Cliente):
    
    banco_de_dados.cadastro_cliente(cliente)

    return cliente

@app.delete('/cliente/{id_cliente}')
def remover_cliente_api(id_cliente):

    banco_de_dados.remover_cadastro(id_cliente)

    return {'Mensagem': 'Usuário removido!'}
