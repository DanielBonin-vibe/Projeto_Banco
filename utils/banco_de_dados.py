import sqlite3

#####################
# Tabelas:

conexao = sqlite3.connect('database/biblioteca.db')
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
    saldo_inicial INTERGER NOT NULL

FOREIGN KEY(cpf_titular) REFERENCES cliente_cpf(cpf))
""")

conexao.commit() 
conexao.close()

#########################################################

def consultar_conta():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    # SELECT mostra as ifnromçãoes que queremos mostrar, FROM aponta a tabela principal
    cursor.execute("""
    SELECT cpf.cliente, conta.cpf_titular FROM cliente
    JOIN conta
        ON cliente.cpf = conta.cpf_titular
    """)
    # ON mostra a relação entre as duas colunas

    consulta = cursor.fetchall()

    for dado in consulta:
        print(dado)

    conexao.commit()
    conexao.close()
#################################################################
# Cadastro

def cadastro_cliente(nome, idade, cpf):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()
    
    cursor.execute("""
    INSERT INTO cliente(nome, idade, cpf)
    VALUES( ?, ?, ?)
    """, (nome, idade, cpf,))

    conexao.commit()
    conexao.close()

def remover_cadastro(id_cliente):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM clientes
    WHERE id_cliente = ?
    """, (id_cliente))

    conexao.commit()
    conexao.close()
#################################################################
def abertura_conta(cpf_titular, saldo_inicial):
    ...

def fechar_conta(id_conta)