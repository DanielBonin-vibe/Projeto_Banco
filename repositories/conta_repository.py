from database.conexao_postgre import conectar

def cadastro_conta(cpf_titular, saldo):
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

def buscar_conta(cpf):
    conexao = conectar()
    cursor = conexao.cursor()  
    try:
        cursor.execute("""
        SELECT * FROM contas
        WHERE cpf_titular = %s
        """, (cpf,))

        resultado = cursor.fetchone()

        return resultado

    except Exception as erro:
        print(f'Erro ao consultar conta: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

def listar_contas():
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT * FROM contas
        """)

        resultado = cursor.fetchall()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao listar contas: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

def consultar_saldo(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT saldo FROM contas
        WHERE cpf_titular = %s
        """, (cpf,))

        resultado = cursor.fetchone()

        return resultado

    except Exception as erro:
        print(f'Erro ao consultar saldo: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()

def encerrar_conta(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        REMOVE FROM contas
        WHERE id_conta = %s
        """, (cpf,))

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

##################################################################################

def deposito_saldo(cpf, deposito):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE contas
            SET saldo = saldo + %s
            WHERE cpf_titular = %s
        """, (deposito, cpf))

        resultado = cursor.rowcount

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao realizar depósito: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()

def saque_saldo(cpf, saque):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE contas
        SET saldo = saldo - %s
        WHERE cpf_titular = %s
        """, (saque, cpf))

        resultado = cursor.rowcount

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao realizar saque: {erro}')
        return 0 
    
    finally:
        cursor.close()
        conexao.close()

def transferencia(cpf_transferidor, cpf_recebedor, transferencia):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE contas
        SET saldo = saldo - %s
        WHERE cpf_titular_transferidor = %s
        """, (transferencia, cpf_transferidor))

        if cursor.rowcount == 0:
            conexao.rollback()
            return 0

        cursor.execute("""
        UPDATE contas
        SET saldo = saldo + %s
        WHERE cpf_titular_recebedor = %s
        """, (transferencia, cpf_recebedor))

        if cursor.rowcount == 0:
            conexao.rollback()
            return 0

        conexao.commit()

        return 1

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao realizar transferência: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()
