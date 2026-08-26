from database.conexao_postgre import conectar

def relatorio_padrao_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM clientes
        ORDER BY id_cliente ASC
        """)

        clientes = cursor.fetchall()

        cursor.execute("""
        SELECT COUNT(*) FROM clientes
        """)

        total = cursor.fetchone()[0]

        return clientes, total

    finally:
        cursor.close()
        conexao.close()

def relatorio_nome_ordem_alfabetica_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM clientes
        ORDER BY nome ASC
        """)

        clientes = cursor.fetchall()

        cursor.execute("""
        SELECT COUNT(*) FROM clientes
        """)

        total = cursor.fetchone()[0]

        return clientes, total

    finally:
        cursor.close()
        conexao.close()

def relatorio_cpf_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM clientes
        ORDER BY cpf ASC
        """)

        clientes = cursor.fetchall()

        cursor.execute("""
        SELECT COUNT(*) FROM clientes
        """)

        total = cursor.fetchone()[0]

        conexao.commit()

        total = cursor.fetchone()[0]

        return clientes, total

    finally:
        cursor.close()
        conexao.close()

def relatorio_faixa_etaria_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
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

        return faixas

    finally:
        cursor.close()
        conexao.close()

def relatorio_padrao_conta():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM contas
        ORDER BY id_conta ASC
        """)

        contas = cursor.fetchall()

        return contas

    finally:
        cursor.close()
        conexao.close()

def relatorio_decrescente_saldo():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM contas
        ORDER BY saldo DESC
        """)

        contas = cursor.fetchall()

        return contas

    finally:
        cursor.close()
        conexao.close()

def relatorio_faixa_saldo():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT
                CASE
                    WHEN saldo < 0 THEN 'Saldo negativo'
                    WHEN saldo <= 5000 THEN 'Nível 1'
                    WHEN saldo <= 20000 THEN 'Nível 2'
                    WHEN saldo <= 100000 THEN 'Nível 3'
                    WHEN saldo <= 250000 THEN 'Nível 4'
                    ELSE 'Nível 5'
                END AS nivel_saldo,
                COUNT(*) AS total_contas
            FROM contas
            GROUP BY nivel_saldo
            ORDER BY nivel_saldo
        """)

        faixas = cursor.fetchall()

        return faixas

    finally:
        cursor.close()
        conexao.close()