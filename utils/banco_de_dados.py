from database.conexao_postgre import conectar

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
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM cliente
    WHERE id_cliente = ?
    """, (id_cliente,))

    quantidade = cursor.rowcount

    conexao.commit()
    conexao.close()

    return quantidade

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

    quantidade = cursor.rowcount

    conexao.commit()
    conexao.close()

    return quantidade

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

    resultado = cursor.fetchone()

    for saldo in resultado:
        print(f'O saldo desta conta é {saldo[0]}')

    conexao.close()

    return resultado

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

    return novo_saldo

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

    return novo_saldo

def transferencia(cpf_titular_transferidor, cpf_titular_recebedor, transferencia):

    if cpf_titular_transferidor == cpf_titular_recebedor:
        raise ValueError ('Não é possível transferir para a própria conta.')

    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT saldo FROM conta 
    WHERE cpf_titular = ?
    """, (cpf_titular_transferidor,))

    resultado = cursor.fetchone()

    if resultado is None:
        conexao.close()
        raise ValueError('Conta do transferidor não encontrada.')

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

    if resultado is None:
        conexao.close()
        raise ValueError('Conta do recebedor não encontrada.')

    saldo_recebedor_inicial = resultado[0]
    saldo_recebedor_final = saldo_recebedor_inicial + transferencia

    cursor.execute("""
    UPDATE conta
    SET saldo = ?
    WHERE cpf_titular = ?
    """, (saldo_recebedor_final, cpf_titular_recebedor))

    conexao.commit()
    conexao.close()

    return saldo_recebedor_final

#########################################################################################
# Relatórios:

# Cliente: 

def relatorio_padrao_cliente():
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM cliente
    """)

    ordem = cursor.fetchall()

    cursor.execute("""
    SELECT COUNT(*) FROM cliente
    """)

    total = cursor.fetchone()[0]

    print('=' * 50)
    print('=' * 15,'RELATÓRIO PADRÃO DE CLIENTES', '=' * 15)
    print('=' * 50)
    for cliente in ordem:
        print(f'ID: {cliente[0]}')
        print(f'NOME: {cliente[1]}')
        print(f'IDADE: {cliente[2]}')
        print(f'CPF: {cliente[3]}')
    print(f'TOTAL DE CLIENTES LISTADOS: {total}')

    conexao.close()

def relatorio_nome_ordem_alfabetica_cliente():
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM cliente
    ORDER BY nome ASC
    """)

    ordem = cursor.fetchall()

    cursor.execute("""
    SELECT COUNT(*) FROM cliente
    """)

    total = cursor.fetchone()[0]

    print('=' * 50)
    print('=' * 15,'RELATÓRIO POR NOME DE CLIENTES', '=' * 15)
    print('=' * 50)
    for cliente in ordem:
        print(f'ID: {cliente[0]}')
        print(f'NOME: {cliente[1]}')
        print(f'IDADE: {cliente[2]}')
        print(f'CPF: {cliente[3]}')
    print(f'TOTAL DE CLIENTES LISTADOS: {total}')

    cursor.close()

def relatorio_cpf_cliente():
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM cliente
    ORDER cpf ASC
    """)

    ordem = cursor.fetchall()

    cursor.execute("""
    SELECT COUNT(*) FROM cliente
    """)

    total = cursor.fetchone()[0]

    print('=' * 50)
    print('=' * 15,'RELATÓRIO POR CPF DE CLIENTES', '=' * 15)
    print('=' * 50)
    for cliente in ordem:
        print(f'ID: {cliente[0]}')
        print(f'NOME: {cliente[1]}')
        print(f'IDADE: {cliente[2]}')
        print(f'CPF: {cliente[3]}')
    print(f'TOTAL DE CLIENTES LISTADOS: {total}')

    cursor.close()

def relatorio_faixa_etaria_cliente():
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * 
        CASE
            WHEN idade BETWEEN 18 AND 25 THEN '18-25'
            WHEN idade BETWEEN 26 AND 35 THEN '26-35'
            WHEN idade BETWEEN 36 AND 50 THEN '36-50'
            ELSE '51+'
        END AS faixa_etaria
        COUNT(*) AS total_clientes
    FROM CLIENTE
    GROUP BY faixa_etaria
    ORDER BY faixa_etaria
    """)
    # 'END AS faixa_etaria'  dá um nome para uma nova coluna criada pelo 'CASE'

    faixas = cursor.fetchall()

    print('=' * 50)
    print('=' * 15, 'RELATÓRIO POR FAIXA ETÁRIA', '=' * 15)
    print('=' * 50)

    for faixa in faixas:
        print(f'FAIXA ETÁRIA: {faixa[0]}')
        print(f'TOTAL DE CLIENTES: {faixa[1]}')
        print()

    conexao.close()

# Conta:

def relatorio_padrao_conta():
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM conta
    """)

    ordem = cursor.fetchall()

    for conta in ordem:
        print(f'ID: {conta[0]}')
        print(f'CPF TITULAR: {conta[1]}')
        print(f'SALDO: {conta[2]}')

    conexao.close()

def relatorio_decrescente_saldo():
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM conta
    ORDER BY saldo DESC
    """)

    ordem = cursor.fetchall()

    for conta in ordem:
        print(f'ID: {conta[0]}')
        print(f'CPF TITULAR: {conta[1]}')
        print(f'SALDO: {conta[2]}')

    conexao.close()

def relatorio_faixa_saldo():
    conexao = sqlite3.connect('database/banco.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT 
        CASE
            WHEN saldo BETWEEN 0 AND 5000 THEN 'Nível 1'
            WHEN saldo BETWEEN 5001 and 20000 THEN 'Nível 2'
            WHEN saldo BETWEEN 20001 and 50000 THEN 'Nível 3'
            WHEN saldo BETWEEN 50001 and 250000 THEN 'Nìvel 4'
            ELSE  'Nível 5'
        END AS nivel_saldo
        COUNT(*) total_contas
    FROM conta
    GROUP BY nivel_saldo
    ORDER BY nivel_saldo
    """)

    faixas = cursor.fetchall()

    print('=' * 50)
    print('=' * 15, 'RELATÓRIO POR NÍVEL DA CONTA', '=' * 15)
    print('=' * 50)
    for faixa in faixas:
        print(f'Nível da conta: {faixa[0]}')
        print(f'Total de contas: {faixa[1]}')
        print()