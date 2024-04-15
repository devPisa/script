import secrets
from conexao_db import conexao_db

class documento():
    
    #Classe responsavel por atribuir os dados e inserir no banco de dados
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    SELECT  resposta.id_resposta FROM pergunta
		            INNER JOIN resposta ON pergunta.id_pergunta = resposta.id_pergunta
                    where pergunta.documento = %s
                    """,(1,))
                retornoDocumento = cursor.fetchall()                
                for documento in retornoDocumento:
                    id_resposta = documento[0]
                    url_documento = secrets.token_urlsafe(32)
                    validado = 1
                    values = (url_documento, id_resposta, validado)                    
                    sql = """
                    INSERT INTO documento (url_documento, id_resposta, validado)
                    VALUES (%s, %s, %s)
                    """
                    cursor.execute(sql, values)
                    conn.commit()
            except Exception as bug:
                print(f"Falha ao inserir cadastro no banco de dados: {bug}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()