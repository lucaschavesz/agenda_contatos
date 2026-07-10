import sqlite3
import tkinter as tk
import time
from tkinter import ttk
from tkinter import messagebox

conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

#funções

def add_contato():
    janelaAdd = tk.Toplevel()
    
    janelaAdd.title('Novo contato')
    
    tk.Label(janelaAdd, text='Nome').pack()
    entradaNome = tk.Entry(janelaAdd)
    entradaNome.pack()
    
    tk.Label(janelaAdd, text='Telefone').pack()
    entradaTel = tk.Entry(janelaAdd)
    entradaTel.pack()
    
    tk.Label(janelaAdd, text= 'E-mail').pack()
    entradaEmail = tk.Entry(janelaAdd)
    entradaEmail.pack()
    
    def salvar():
        nome = entradaNome.get()
        telefone = entradaTel.get()
        email = entradaEmail.get()
        
        cursor.execute("""INSERT INTO contatos (nome, telefone, email)
                       VALUES (?,?,?)""", (nome, telefone, email))
        
        conexao.commit()
        
        messagebox.showinfo(
        "Sucesso",
        "Contato salvo com sucesso!"
        )
                
        janelaAdd.destroy()
        
    
    tk.Button(janelaAdd, text='Salvar', command=salvar).pack()
    
               

def lista_contatos():
    
    janelaLista = tk.Toplevel()
    janelaLista.title('Lista de contatos')
    
    tree = ttk.Treeview(
        janelaLista,
        columns=('ID', 'Nome', 'Telefone', 'E-mail'),
        show='headings'
        
    )    
    tree.heading('ID', text='ID')
    tree.heading('Nome', text='Nome')
    tree.heading('Telefone', text='Telefone')
    tree.heading('E-mail', text='E-mail')
    
    tree.column("ID", width=50)
    tree.column("Nome", width=150)
    tree.column("Telefone", width=120)
    tree.column("E-mail", width=200)
    
    tree.pack(fill='both', expand=True)
    
    cursor.execute("""SELECT * FROM contatos""")
    lista = cursor.fetchall()
    
    for i in lista:
        tree.insert("", tk.END, values= i)
    

def busca_contato():
    
    janelaBusca = tk.Toplevel()
    janelaBusca.title('Buscar contato')
    
    tk.Label(janelaBusca, text='Nome').pack()
    
    nomeEntrada = tk.Entry(janelaBusca)
    nomeEntrada.pack()
    
    def buscar():
        nome = nomeEntrada.get()
        
        
        
        tree = ttk.Treeview(
        janelaBusca,
        columns=('ID', 'Nome', 'Telefone', 'E-mail'),
        show='headings'
        )    
        tree.heading('ID', text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Telefone', text='Telefone')
        tree.heading('E-mail', text='E-mail')
    
        tree.column("ID", width=50)
        tree.column("Nome", width=150)
        tree.column("Telefone", width=120)
        tree.column("E-mail", width=200)
    
        tree.pack(fill='both', expand=True)
    
        cursor.execute("""SELECT * FROM contatos
                       WHERE nome = ?""", (nome,))
        
        result = cursor.fetchall()
    
        for i in result:
            tree.insert("", tk.END, values= i)
            
    tk.Button(janelaBusca, text='Buscar', command=buscar).pack()
            
            
            
            
            
            
def atualiza_contato():
    janelaAtt = tk.Toplevel()
    janelaAtt.title('Atualizar contato')
    
    tk.Label(janelaAtt, text='ID do contato').pack()
    entradaID = tk.Entry(janelaAtt)
    entradaID.pack()
    
    tk.Label(janelaAtt, text='Novo nome').pack()
    novoNome = tk.Entry(janelaAtt)
    novoNome.pack()
    
    tk.Label(janelaAtt, text='Novo telefone').pack()
    novoTel = tk.Entry(janelaAtt)
    novoTel.pack()
    
    tk.Label(janelaAtt, text='Novo e-mail').pack()
    novoEmail = tk.Entry(janelaAtt)
    novoEmail.pack()
    
    def salvar_att():
        id = entradaID.get()
        nome = novoNome.get()
        telefone = novoTel.get()
        email = novoEmail.get()
        
        cursor.execute("""SELECT * FROM contatos
                       WHERE id = ?""", (id,))
        
        x = cursor.fetchone()
        
        if x:
        
            cursor.execute("""UPDATE contatos
                       SET nome = ?, telefone = ?, email = ?
                       WHERE id = ?""",(nome, telefone, email, id))
            
               
            
            conexao.commit()
            
            messagebox.showinfo(
            "Sucesso",
            "Contato atualizado com sucesso!"
            )
            
            janelaAtt.destroy()
        else:
            
            tk.Label(janelaAtt, text='Contato não existente').pack()
            janelaAtt.destroy()
    
    tk.Button(janelaAtt, text='Salvar', command=salvar_att).pack()
    
def exclui_contato():
    janelaDel = tk.Toplevel()
    janelaDel.title('Excluir contato')
    
    tk.Label(janelaDel, text='ID do contato').pack()
    
    entradaId = tk.Entry(janelaDel)
    entradaId.pack()
    
    def salvar_exclui():
    
        id = entradaId.get()
        idInt = int(id)
    
        cursor.execute("""SELECT * FROM contatos
                   WHERE id = ?""",(idInt,))
    
        linha = cursor.fetchall()
    
        if linha:
            cursor.execute("""DELETE FROM contatos
                       where id = ?""",(idInt,))
        
            conexao.commit()
        
            messagebox.showinfo(
            "Sucesso",
            "Contato excluído com sucesso!"
            )
            
            janelaDel.destroy()
        else:
            messagebox.showinfo(
            "Erro",
            "Contato não existente!"
            )
            janelaDel.destroy()
    tk.Button(janelaDel, text='Salvar', command= salvar_exclui).pack()