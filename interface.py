import tkinter as tk 
from functions.funcoes import add_contato, lista_contatos, busca_contato, exclui_contato, atualiza_contato
import sqlite3

conexao = sqlite3.connect('data/dados.db')
cursor = conexao.cursor()

#cria tabela contatos
cursor.execute("""CREATE TABLE IF NOT EXISTS contatos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
telefone TEXT,
email TEXT
)""")

conexao.commit()

janela = tk.Tk()

janela.title('Agenda de Contatos')
janela.geometry('400x300')

tk.Label(janela, text='AGENDA DE CONTATOS').pack()

tk.Button(janela, text='Adicionar contato', command= add_contato).pack()
tk.Button(janela, text='Excluir contato', command=exclui_contato).pack()
tk.Button(janela, text='Listar contatos', command=lista_contatos).pack()
tk.Button(janela, text='Buscar contato', command=busca_contato).pack()
tk.Button(janela, text='Atualizar contato', command=atualiza_contato).pack()

janela.mainloop()
conexao.close()
