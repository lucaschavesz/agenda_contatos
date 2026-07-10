import sqlite3

conexao = sqlite3.connect('dados.db')

cursor = conexao.cursor()

#cria tabela contatos
cursor.execute("""CREATE TABLE IF NOT EXISTS contatos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
telefone TEXT,
email TEXT
)""")

conexao.commit()

conexao.close()
