
# Cliente: 

def relatorio_padrao_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM clientes
    ORDER BY id_cliente ASC
    """)

    ordem = cursor.fetchall()

    cursor.execute("""
    SELECT COUNT(*) FROM clientes
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

    cursor.close()
    conexao.close()

    return ordem, total

def relatorio_nome_ordem_alfabetica_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM clientes
    ORDER BY nome ASC
    """)

    ordem = cursor.fetchall()

    cursor.execute("""
    SELECT COUNT(*) FROM clientes
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
    conexao.close()

    return ordem, total

def relatorio_cpf_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM clientes
    ORDER BY cpf ASC
    """)

    ordem = cursor.fetchall()

    cursor.execute("""
    SELECT COUNT(*) FROM clientes
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
    conexao.close()

    return ordem, total

def relatorio_faixa_etaria_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT 
        CASE
            WHEN idade >= 17 THEN '-17'
            WHEN idade BETWEEN 18 AND 25 THEN '18-25'
            WHEN idade BETWEEN 26 AND 35 THEN '26-35'
            WHEN idade BETWEEN 36 AND 50 THEN '36-50'
            ELSE '51+'
        END AS faixa_etaria,
        COUNT(*) AS total_clientes
    FROM clientes
    GROUP BY faixa_etaria
    ORDER BY faixa_etaria
    """)

    faixas = cursor.fetchall()

    print('=' * 50)
    print('=' * 15, 'RELATÓRIO POR FAIXA ETÁRIA', '=' * 15)
    print('=' * 50)

    for faixa in faixas:
        print(f'FAIXA ETÁRIA: {faixa[0]}')
        print(f'TOTAL DE CLIENTES: {faixa[1]}')
        print()

    cursor.close()
    conexao.close()

    return faixas

# Conta:

def relatorio_padrao_conta():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM contas
    ORDER BY id_conta ASC
    """)

    ordem = cursor.fetchall()

    for conta in ordem:
        print(f'ID: {conta[0]}')
        print(f'CPF TITULAR: {conta[1]}')
        print(f'SALDO: {conta[2]}')

    cursor.close()
    conexao.close()

    return ordem

def relatorio_decrescente_saldo():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM contas
    ORDER BY saldo DESC
    """)

    ordem = cursor.fetchall()

    for conta in ordem:
        print(f'ID: {conta[0]}')
        print(f'CPF TITULAR: {conta[1]}')
        print(f'SALDO: {conta[2]}')

    cursor.close()
    conexao.close()

    return ordem 

def relatorio_faixa_saldo():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT 
        CASE
            WHEN saldo < 0 THEN 'Saldo negativo'
            WHEN saldo <= 5000 THEN 'Nível 1'
            WHEN saldo <= 20000 THEN 'Nível 2'
            WHEN saldo <= 50000 THEN 'Nível 3'
            WHEN saldo <= 250000 THEN 'Nível 4'
            ELSE 'Nível 5'
        END AS nivel_saldo,
        COUNT(*) total_contas
    FROM contas
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

    return faixas