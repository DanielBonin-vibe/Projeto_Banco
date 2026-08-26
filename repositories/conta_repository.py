from database.conexao_postgre import conectar

def abertura_conta(cpf_titular, saldo):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO contas(cpf_titular, saldo)
        VALUES (%s, %s)
        """, (cpf_titular, saldo))

        resultado = cursor.rowcount

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao abrir conta: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

def fechar_conta(id_conta):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        REMOVE FROM contas
        WHERE id_conta = %s
        """, (id_conta,))

        resultado = cursor.rowcount

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao fechar conta: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

def consultar_conta():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT clientes.nome, clientes.cpf, contas.id_conta, contas.saldo FROM clientes
        JOIN contas
            ON clientes.cpf = contas.cpf_titular
        """)

        resultado = cursor.fetchall()

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao consulta conta: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

def buscar_cliente_e_conta(cpf_buscado):
    conexao = conectar()
    cursor = conexao.cursor()  
    try:
        cursor.execute("""
        SELECT clientes.nome, clientes.idade, clientes.cpf, contas.id_conta, contas.saldo FROM clientes
        JOIN contas
            ON clientes.cpf = contas.cpf_titular
        WHERE clientes.cpf = %s
        """, (cpf_buscado,))

        resultado = cursor.fetchone()
        conexao.commit()

        return resultado

    except Exception as erro:
        print(f'Erro ao consultar conta: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

###################################################################################
# Ações bancárias:

def consulta_saldo(cpf_buscado):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT saldo FROM contas
        WHERE cpf_titular = %s
        """, (cpf_buscado,))

        resultado = cursor.fetchone()

        return resultado

    except Exception as erro:
        print(f'Erro ao consultar saldo: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()


def deposito_saldo(cpf_do_titular, deposito):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE contas
            SET saldo = saldo + %s
            WHERE cpf_titular = %s
            RETURNING saldo
        """, (deposito, cpf_do_titular))

        resultado = cursor.fetchone()

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao realizar depósito: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()

def sacar_saldo(cpf_do_titular, saque):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE contas
        SET saldo = saldo - %s
        WHERE cpf_titular = %s
        RETURNING saldo
        """, (saque, cpf_do_titular))

        resultado = cursor.fetchone()

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao realizar saque: {erro}')
        return 0 
    finally:
        cursor.close()
        conexao.close()

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
