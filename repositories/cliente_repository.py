from database.conexao_postgre import conectar

def cadastro_cliente(nome, idade, cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO clientes(nome, idade, cpf)
        VALUES(%s, %s, %s)
        """, (nome, idade, cpf))

        resultado = cursor.rowcount

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao cadastrar cliente: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()

def remover_cadastro(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        DELETE FROM clientes
        WHERE id_cliente = %s
        """, (cpf,))

        quantidade = cursor.rowcount

        conexao.commit()

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao remover cliente: {erro}')

        return 0
    finally:
        cursor.close()
        conexao.close()

    return quantidade

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()  

    try:
        cursor.execute("""
        SELECT * FROM clientes
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'erro ao listar clientes: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()
