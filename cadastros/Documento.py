import secrets;
from conexao_db import conexao_db
from Resposta import Resposta
from Pergunta import Pergunta

class Documento():

    #Função responsavel por gerar um URL aleatório de 32bit
    #Classe associada ao banco, responsavel por atribuir todos os dados da tabela
    @classmethod
    def gerarDocumento(cls):
        url_documento = secrets.token_urlsafe(32);
        return(url_documento)
    
    #Classe responsavel por pegar os dados que foram atribuidos e inserir no banco de dados
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
                #Aqui estamos associando tabela de pergunta, resposta e documento
                #onde o id_reposta tem que ser = id_pergunta
                #usamos o retorno da função id_reposta e id_pergunta para configurar
                #os parametros do select
                cursor.execute  ("""
                                SELECT Pergunta.documento
                                FROM Pergunta
                                INNER JOIN Resposta ON Pergunta.id_pergunta = Resposta.id_pergunta
                                INNER JOIN Documento On Resposta.id_resposta = Documento.id_documento
                                WHERE Resposta.id_resposta = %s AND  Pergunta.id_pergunta = %s
                                """, (id_resposta,id_pergunta))
                #A partir da tumpla de resultados retornados, pegamos a posição 2
                #referente ao atributo documento
                documentoAnexo = cursor.fetchall()[2]
                #Se atributo for = 0 ele instasia um novo documento
                if documentoAnexo == 0:
                    return cls.gerarDocumento()
                else:
                    return None
            except Exception as bug:
                print(f"Falha consultar id_formulario no banco de dados: {bug}")
            finally:
                cursor.close()
                conn.close()
