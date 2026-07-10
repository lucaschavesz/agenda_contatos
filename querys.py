import sqlite3

conexao = sqlite3.connect('dados.db')

cursor = conexao.cursor()


conexao.commit()

conexao.close()
