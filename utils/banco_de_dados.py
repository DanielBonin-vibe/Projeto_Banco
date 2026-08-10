import sqlite3

#####################
# Tabelas:

conexao = sqlite3.connect('database/biblioteca.db')
cursor = conexao.cursor()