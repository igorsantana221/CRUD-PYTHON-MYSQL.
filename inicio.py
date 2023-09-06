import pymysql.cursors


#CRUD PYTHON + MYSQL Conexão

con = pymysql.connect(
    host = "127.0.0.1",
    user="root",
    password="",
    port=3306,
    db="aulapythonfull",       
    charset="utf8mb4",
    cursorclass= pymysql.cursors.DictCursor)

#7 - CRUD PYTHON + MYSQL Criando tabela e removendo tabela.

def criarTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"CREATE TABLE {nomeTabela} (nome varchar(50))")
        print ("tabela criada com sucesso")
        
    except Exception as e:
        print(f'Erro:{e}')

    con.close()
    

    

def dropTable(dropTable):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DROP TABLE {dropTable}")
        print ('Tabela excluida com sucesso')
    except Exception as e:
        print (f'Erro:{e}')
        
    con.close()

#8 - CRUD PYTHON + MYSQL Insert into 

def insereTabela(nome):

    try:
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO teste12 values ('{nome}')")
        print('valor inserido com sucesso')
    except Exception as e:
        print(f"erro: {e}")
        
    con.close()
    
#selecionando tabela  
        
def selectTable(tabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"Select * FROM {tabela}")
            resultado = cursor.fetchall()
        print(f'Valor: {resultado}')
    except Exception as e:
        print(f"erro: {e}")
        
    con.close()
    
    
#10 - CRUD PYTHON + MYSQL UPDATE 

def updateTable(pri_update, sec_update):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"UPDATE teste12 set nome = '{pri_update}' WHERE nome = '{sec_update}'")
            
        print('Update realizado com sucesso.')
    except Exception as e:
        print(f"erro: {e}")
        
    con.close()

#11 - CRUD PYTHON + MYSQL Delete

def deleteTable(delete):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DELETE FROM teste12 WHERE nome = '{delete}'")
            
        print('Deteletado com sucesso.')
    except Exception as e:
        print(f"erro: {e}")
        
        con.close()
        


