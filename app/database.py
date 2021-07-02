import pymysql

def connection():
    try:
        db = pymysql.connect(host="jobs.visie.com.br",
                            user="rafaelpaixao",
                            passwd="cmFmYWVscGFp",
                            db="rafaelpaixao",
                            port=3306)
        return db

    except pymysql.Error as e:
        print(f'Erro a conectar ao banco: {e}')
        
def select_pessoas():
  with connection() as connect:
    with connect.cursor() as cursor:
      cursor.execute("SELECT nome,rg, data_admissao,  id_pessoa FROM pessoas")
    return cursor.fetchall()

def save_pessoas(val):
  print(val)
  with connection() as connect:
    with connect.cursor() as cursor:
      cursor.execute(f"INSERT INTO pessoas (nome, rg, cpf, data_nascimento, data_admissao, funcao) VALUES ('{val['nome']}','{val['rg']}','{val['cpf']}','{val['data_nasc']}','{val['data']}', '{val['funcao']}')")
    connect.commit()
  
def delete_pessoas(id):
  with connection() as connect:
    with connect.cursor() as cursor:
      cursor.execute(f'DELETE FROM pessoas WHERE id_pessoa= "{id}"')
    connect.commit()    
