import time
import sqlite3

conexao = sqlite3.connect('dados.db')

cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    email TEXT)""")



print('=======AGENDA DE CONTATOS=======')

while(True):
    print("""Funcionalidades:
          
             1 - Adicionar contato
             2 - Listar contatos
             3 - Buscar contato pelo nome
             4 - Atualizar contato
             5 - Excluir contato
             6 - Sair""")
    
    opcao = int(input('Escolha uma opção: '))
    
    if opcao == 1:
        print()
        nome = input('Insira o nome do contato: ')
        
        telefone = input('Insira o telefone do contato: ')
        
        email = input('Insira o e-mail do contato: ')
        while '@' not in email:
            email = input('E-mail inválido. Digite novamente:')
        
        
        cursor.execute("""INSERT INTO contatos 
                       (nome, telefone, email) VALUES (?,?,?)""", (nome, telefone, email))
        
        conexao.commit()
        print()
        time.sleep(2)
        print('Contato adicionado com sucesso!')
        print()
        time.sleep(2)        
    
    elif opcao == 2:
        
        cursor.execute('SELECT * FROM contatos')
        
        items = cursor.fetchall()
        
        print()
        for item in items:
            print(item)
        print()
        time.sleep(2)
            
    elif opcao == 3:
        print()
        nomeCtt = input('Informe o nome do contato que você busca: ')
        cursor.execute("""SELECT * FROM contatos
                       WHERE nome = ? """, (nomeCtt,))
        
        lista = cursor.fetchall()
        
        print()
        for item in lista:
            print(item)
            
        print()
        time.sleep(2)
            
    elif opcao == 4:
        print()
        id = input('Insira o ID do contato que será atualizado: ')
        
        cursor.execute("""SELECT * FROM contatos
                       where id = ? """, (id,))
        
        ctt = cursor.fetchone()
        
        if ctt:
            novoNome = input('Insira o novo nome: ')
            novoTel = input('Insira o novo telefone: ')
            novoEmail = input('Insira o novo email: ')
            
            cursor.execute("""UPDATE contatos
                           SET nome = ?, telefone = ?, email = ?
                           where id = ?""", (novoNome, novoTel, novoEmail, id))
            
            conexao.commit()
            
            print()
            time.sleep(2)
            print('Contato atualizado com sucesso!')
            print()
            time.sleep(2)
        else:
            print()
            print('Contato não encontrado.')
            print()
            time.sleep(2)
            
    elif opcao == 5:
        print()
        idDel = input('Insira o ID do contato que será apagado: ')
        
        cursor.execute("""SELECT * FROM contatos
                       WHERE id = ?""", (idDel,))
        
        x = cursor.fetchone()
        
        if x:
            cursor.execute("""DELETE FROM contatos
                           WHERE id = ?""", (idDel,))
            conexao.commit()
            print()
            print('Contato excluído com sucesso.')
            print()
            time.sleep(2)            
        else:
            print()
            print('Contato não encontrado.')
            print()
            time.sleep(2)
    
    elif opcao == 6:
        print()
        print('Saindo...')
        break
    
    else:
        print()
        print('Opção inválida, escolha uma opção de 1 a 6.')
        print()
        time.sleep(2)   
        
conexao.close()         
    

            
        