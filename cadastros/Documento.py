import secrets;
from conexao_db import conexao_db
from Resposta import Resposta
from Pergunta import Pergunta

class Documento():

    @classmethod
    def gerarDocumento(cls):
        url_documento = secrets.token_urlsafe(32);
        return(url_documento)
    
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                values = cls.gerarDocumento()
                sql =   """
                        INSERT INTO Documento (urd_documento)
                        VALUES (%s)
                        """
                cursor.execute(sql, values)
                conn.commit()
                print('Documento cadastrado')
            except Exception as bug:
                print(f"Falha ao inserir documento no banco de dados: {bug}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
    
    @classmethod
    def respostaDocumento(cls):
        id_resposta = Resposta.id_resposta()
        id_pergunta = Pergunta.id_pergunta()     
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute  ("""
                                SELECT Pergunta.documento
                                FROM Pergunta
                                INNER JOIN Resposta ON Pergunta.id_pergunta = Resposta.id_pergunta
                                INNER JOIN Documento On Resposta.id_resposta = Documento.id_documento
                                WHERE Resposta.id_resposta = %s AND  Pergunta.id_pergunta = %s
                                """, (id_resposta,id_pergunta))
                documentoAnexo = cursor.fetchall()[2]
                if documentoAnexo == 0:
                    return cls.gerarDocumento()
                else:
                    return None
            except Exception as bug:
                print(f"Falha consultar id_formulario no banco de dados: {bug}")
            finally:
                cursor.close()
                conn.close()
