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
    saldo INTERGER NOT NULL

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
# Cliente

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
    """, (id_cliente,))

    conexao.commit()
    conexao.close()

def listar_clientes():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()  

    cursor.execute("""
    SELECT * FROM cliente
    """)

    ditagem = cursor.fetchall()

    for cliente in ditagem:
        print(cliente)

    cursor.execute("""
    SELECT COUNT(*) FROM cliente
    """)

    quantidade = cursor.fetchone()

    print(f'Total de clientes: {quantidade[0]}') # Precisamos especificar
    # Count retorna apenas uma linha, por isso devemos passar o [0].

    conexao.commit()
    conexao.close()

#################################################################
# Conta:
def abertura_conta(cpf_titular, saldo):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO conta(cpf_titular, saldo)
    VALUES(?, ?)
    """, (cpf_titular, saldo,))

    conexao.commit()
    conexao.close()

def fechar_conta(id_conta):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    REMOVE FROM conta
    WHERE id_conta = ?
    """, (id_conta,))

    conexao.commit()
    conexao.close()

def buscar_cliente_e_conta(cpf_buscado):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()  

    cursor.execute("""
    SELECT cliente.nome, cliente.idade, cliente.cpf,
    conta.id_conta, conta.saldo
    FROM cliente
    LEFT JOIN conta
        ON cliente.cpf = conta.cpf_titular
    WHERE cliente.cpf = ?
    """, (cpf_buscado,))

# No ON, ele quer dizer 'Pegue o CPF do cliente'
# E procure esse mesmo CPF como titular da conta,s e forem iguais,
# O SQLite entende que a conta pertence áquele cliente.

    resultado = cursor.fetchone()

    conexao.commit()
    conexao.close()

    print(resultado)

#############################################################
# Ações:

def consulta_saldo(cpf_buscado):
    conexao = sqlite3.connect('database/biblioteca.db')
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
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT saldo FROM conta
    WHERE cpf_do_titular = ?
    """, (cpf_do_titular,))

    resultado = cursor.fetchone()

    saldo_inicial = resultado[0]
    novo_saldo = saldo_inicial + deposito

    cursor.execute("""
    SELECT saldo FROM conta
    SET saldo = ?
    WHERE cpf_titular = ? 
    """, (novo_saldo, cpf_do_titular))
    
    conexao.commit()
    conexao.close()

def sacar_saldo(cpf_do_titular, saque):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT saldo FROM conta
    WHERE cpf_titular = ?
    """, (cpf_do_titular,))

    resultado = cursor.fetchone()

    saldo_inicial = resultado[0]
    novo_saldo = saldo_inicial - saque

    cursor.execute("""
    SELECT saldo FROM conta
    SET saldo = ?
    WHERE cpf_titular = ?
    """, (novo_saldo, cpf_do_titular))

    conexao.commit()
    conexao.close()

def 