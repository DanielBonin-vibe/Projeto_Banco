

import json

def salvar_json(caminho, dados):  # Caminho é aonde o arquivo será salvo, dados é o que será salvo    # Ex.: salvar_json("dados/clientes.json", lista_clientes)
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)  # json.dump grava o dicionário em clientes.json

def carregar_json(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)