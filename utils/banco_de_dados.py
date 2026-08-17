import sqlite3

#####################
# Tabelas:

conexao = sqlite3.connect('database/banco.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE cliente IF IT NOT EXISTS(
    id_cliente INTERGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTERGER NOT NULL,
    cpf TEXT NOT NULL UNIQUE)
""")

cursor.execute("""
CREATE TABLE conta IF IT NOT EXISTS( 
    id_conta PRIMARY KEY AUTOINCREMENT,
    cpf_titular TEXT NOT NULL,
    saldo INTERGER NOT NULL

FOREIGN KEY(cpf_titular) REFERENCES cliente_cpf(cpf))
""")

conexao.commit() 
conexao.close()



#################################################################
# Cliente

def cadastro_cliente(nome, idade, cpf):
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()
    
    cursor.execute("""
    INSERT INTO cliente(nome, idade, cpf)
    VALUES( ?, ?, ?)
    """, (nome, idade, cpf,))

    conexao.commit()
    conexao.close()

def remover_cadastro(id_cliente):
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM cliente
    WHERE id_cliente = ?
    """, (id_cliente,))

    conexao.commit()
    conexao.close()

def listar_clientes():
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()  

    cursor.execute("""
    SELECT * FROM cliente
    """)

    listagem = cursor.fetchall()

    conexao.close()

    return listagem

#################################################################
# Conta:
def abertura_conta(cpf_titular, saldo):
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO conta(cpf_titular, saldo)
    VALUES(?, ?)
    """, (cpf_titular, saldo,))

    conexao.commit()
    conexao.close()

def fechar_conta(id_conta):
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    REMOVE FROM conta
    WHERE id_conta = ?
    """, (id_conta,))

    conexao.commit()
    conexao.close()


def consultar_conta():
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT cpf.cliente, conta.cpf_titular FROM cliente
    JOIN conta
        ON cliente.cpf = conta.cpf_titular
    """)

    consulta = cursor.fetchall()

    for dado in consulta:
        print(f"CPF do cliente: {dado[0]} | CPF do titular: {dado[1]}")

    conexao.close()

    return consulta

def buscar_cliente_e_conta(cpf_buscado):
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()  

    cursor.execute("""
    SELECT cliente.nome, cliente.idade, cliente.cpf,
    conta.id_conta, conta.saldo
    FROM cliente
    LEFT JOIN conta
        ON cliente.cpf = conta.cpf_titular
    WHERE cliente.cpf = ?
    """, (cpf_buscado,))

    resultado = cursor.fetchone()

    conexao.close()

    return resultado

#############################################################
# Ações:

def consulta_saldo(cpf_buscado):
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT saldo FROM conta
    WHERE cpf_titular = ?
    """, (cpf_buscado,))

    resultados = cursor.fetchall()

    for saldo in resultados:
        print(f'O saldo desta conta é {saldo[0]}')

    conexao.close()

def deposito_saldo(cpf_do_titular, deposito):
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT saldo FROM conta
    WHERE cpf_do_titular = ?
    """, (cpf_do_titular,))

    resultado = cursor.fetchone()

    saldo_inicial = resultado[0]
    novo_saldo = saldo_inicial + deposito

    cursor.execute("""
    UPDATE conta
    SET saldo = ?
    WHERE cpf_titular = ? 
    """, (novo_saldo, cpf_do_titular))
    
    conexao.commit()
    conexao.close()

def sacar_saldo(cpf_do_titular, saque):
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT saldo FROM conta
    WHERE cpf_titular = ?
    """, (cpf_do_titular,))

    resultado = cursor.fetchone()

    saldo_inicial = resultado[0]
    novo_saldo = saldo_inicial - saque

    cursor.execute("""
    UPDATE conta
    SET saldo = ?
    WHERE cpf_titular = ?
    """, (novo_saldo, cpf_do_titular))

    conexao.commit()
    conexao.close()

def transferencia(cpf_titular_transferidor, cpf_titular_recebedor, transferencia):
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT saldo FROM conta 
    WHERE cpf_titular = ?
    """, (cpf_titular_transferidor,))

    resultado = cursor.fetchone()
    saldo_transferidor_inicial = resultado[0]
    saldo_transferidor_final = saldo_transferidor_inicial - transferencia

    cursor.execute("""
    UPDATE conta
    SET saldo = ?
    WHERE cpf_titular = ?
    """, (saldo_transferidor_final, cpf_titular_transferidor))

    cursor.execute("""
    SELECT saldo FROM conta
    WHERE cpf_titular = ?
    """, (cpf_titular_recebedor,))

    resultado = cursor.fetchone()
    saldo_recebedor_inicial = resultado[0]
    saldo_recebedor_final = saldo_recebedor_inicial + transferencia

    cursor.execute("""
    UPDATE conta
    SET saldo = ?
    WHERE cpf_titular = ?
    """, (saldo_recebedor_final, cpf_titular_recebedor))

    conexao.commit()
    conexao.close()