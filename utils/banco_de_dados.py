from database.conexao_postgre import conectar

#################################################################
# Cliente

def cadastro_cliente(nome, idade, cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""
    INSERT INTO clientes(nome, idade, cpf)
    VALUES(%s, %s, %s)
    """, (nome, idade, cpf))

    conexao.commit()
    cursor.close()
    conexao.close()

def remover_cadastro(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM clientes
    WHERE id_cliente = %s
    """, (id_cliente,))

    quantidade = cursor.rowcount

    conexao.commit()
    cursor.close()
    conexao.close()

    return quantidade

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()  

    cursor.execute("""
    SELECT * FROM clientes
    """)

    listagem = cursor.fetchall()

    cursor.close()
    conexao.close()

    return listagem

#################################################################
# Conta:
def abertura_conta(cpf_titular, saldo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO contas(cpf_titular, saldo)
    VALUES (%s, %s)
    """, (cpf_titular, saldo))

    conexao.commit()
    cursor.close()
    conexao.close()

def fechar_conta(id_conta):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    REMOVE FROM contas
    WHERE id_conta = %s
    """, (id_conta,))

    quantidade = cursor.rowcount

    conexao.commit()
    cursor.close()
    conexao.close()

    return quantidade

def consultar_conta():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT clientes.nome, clientes.cpf, contas.id_conta, contas.saldo FROM clientes
    JOIN contas
        ON clientes.cpf = contas.cpf_titular
    """)

    consulta = cursor.fetchall()

    for dado in consulta:
        print(
            f"Cliente: {dado[0]} | "
            f"CPF: {dado[1]} | "
            f"Conta: {dado[2]} | "
            f"Saldo: R$ {dado[3]}"
        )


    cursor.close()
    conexao.close()

    return consulta

def buscar_cliente_e_conta(cpf_buscado):
    conexao = conectar()
    cursor = conexao.cursor()  

    cursor.execute("""
    SELECT clientes.nome, clientes.idade, clientes.cpf, contas.id_conta, contas.saldo FROM clientes
    JOIN contas
        ON clientes.cpf = contas.cpf_titular
    WHERE clientes.cpf = %s
    """, (cpf_buscado,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado

#############################################################
# Ações:

def consulta_saldo(cpf_buscado):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT saldo FROM contas
    WHERE cpf_titular = %s
    """, (cpf_buscado,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado

def deposito_saldo(cpf_do_titular, deposito):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE contas
        SET saldo = saldo + %s
        WHERE cpf_titular = %s
        RETURNING saldo
    """, (deposito, cpf_do_titular))

    resultado = cursor.fetchone()

    conexao.commit()
    cursor.close()
    conexao.close()

    if resultado:
        return resultado[0]

    return None

def sacar_saldo(cpf_do_titular, saque):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE contas
    SET saldo = saldo - %s
    WHERE cpf_titular = %s
    RETURNING saldo
    """, (saque, cpf_do_titular))

    resultado = cursor.fetchone()

    conexao.commit()
    cursor.close()
    conexao.close()

    if resultado:
        return resultado[0]

    return None

def transferencia(cpf_titular_transferidor, cpf_titular_recebedor, transferencia):

    if cpf_titular_transferidor == cpf_titular_recebedor:
        raise ValueError ('Não é possível transferir para a própria conta.')

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE contas
        SET saldo = saldo - %s
        WHERE cpf_titular_transferidor = %s
        RETURNING saldo
        """, (transferencia, cpf_titular_transferidor))

        resultado_transferidor = cursor.fetchone()

        if resultado_transferidor is None:
            raise ValueError("Conta do transferidor não encontrada.")

        cursor.execute("""
        UPDATE contas
        SET saldo = saldo + %s
        WHERE cpf_titular_recebedor = %s
        RETURNING saldo
        """, (transferencia, cpf_titular_recebedor))

        resultado_recebedor = cursor.fetchone()

        if resultado_recebedor is None:
            raise ValueError('Conta do recebedor não encontrada.')

        conexao.commit()

        return resultado_recebedor[0]

    except:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

#########################################################################################
# Relatórios:

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