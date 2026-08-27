from dotenv import load_dotenv
import psycopg, os

load_dotenv()


def conectar():
    return psycopg.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('BD_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
    )


print("Tentando conectar...")

try:
    conexao = conectar()
    print("Conexão realizada com sucesso!")
    conexao.close()

except Exception as erro:
    print("Erro ao conectar:")
    print(erro)
