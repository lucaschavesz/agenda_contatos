import sqlite3

conexao = sqlite3.connect('dados.db')

cursor = conexao.cursor()

cursor.execute("""DELETE * FROM contatos""")

conexao.commit()

conexao.close()