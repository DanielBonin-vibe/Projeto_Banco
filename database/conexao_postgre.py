import psycopg

def conectar():
    return psycopg.connect(
        dbname='projeto_banco',
        user='postgres',
        password='B@nin180506',
        host='localhost',
        port='5432',
        connect_timeout=5
    )


print("Tentando conectar...")

try:
    conexao = conectar()

    print("Conexão realizada com sucesso!")

    conexao.close()

except Exception as erro:
    print("Erro ao conectar:")
    print(erro)
conexao.close()