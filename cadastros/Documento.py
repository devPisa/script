import secrets
from conexao_db import conexao_db
from Resposta import Resposta
from Pergunta import Pergunta

class Documento():
    
    @classmethod
    def respostaDocumento(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    SELECT  Resposta.id_resposta FROM Pergunta
		            INNER JOIN Resposta ON Pergunta.id_pergunta = Resposta.id_pergunta
                    where Pergunta.documento = %s
                    """,(1,))

                documentos_faltantes = cursor.fetchall()
                print(documentos_faltantes)
                
                for documento in documentos_faltantes:
                    id_resposta = documento[0]
                    print(f"resposta ==> {id_resposta}")
                    url_documento = secrets.token_urlsafe(32)
                    validado = 1
                    values = (url_documento, id_resposta, validado)
                    print(url_documento)
                    
                    sql = """
                    INSERT INTO Documento (url_documento, id_resposta, validado)
                    VALUES (%s, %s, %s)
                    """
                    cursor.execute(sql, values)
                
                conn.commit()  # Movendo o commit para fora do loop
                print("Atribuição de documentos concluída.")
            except Exception as e:
                print(f"Falha ao consultar o banco de dados: {e}")  # Mensagem de erro mais descritiva
            finally:
                cursor.close()
                conn.close()

# Chamada da função para testar
















# import secrets;
# from conexao_db import conexao_db
# from Resposta import Resposta
# from Pergunta import Pergunta

# class Documento():
    
#     #Função responsavel por gerar um URL aleatório de 32bit
#     #Classe associada ao banco, responsavel por atribuir todos os dados da tabela
#     @classmethod
#     def respostaDocumento(cls):
#         conn = conexao_db()
#         if conn:
#             cursor = conn.cursor()
#             try:
#                 cursor.execute("""
#                     SELECT  Resposta.id_resposta, Pergunta.documento FROM Pergunta
# 		            INNER JOIN Resposta ON Pergunta.id_pergunta = Resposta.id_pergunta
#                     where Pergunta.documento = %s
#                     """,(1,))

#                 documentos_faltantes = cursor.fetchall()
                
#                 for documento in documentos_faltantes:
#                     id_pergunta, documento_atual = documento
#                     if documento_atual == 1:
#                         id_resposta = Resposta.id_resposta()
#                         url_documento = secrets.token_urlsafe(32)
#                         validado = 1
#                         values = (url_documento, id_resposta, validado)
#                         print(url_documento)
#                         sql =   """
#                         INSERT INTO Documento (url_documento, id_resposta, validado)
#                         VALUES (%s, %s, %s)
#                         """
#                 cursor.execute(sql, values)
#                 conn.commit()
#                 print("Atribuição de documentos concluída.")
#             except Exception as bug:
#                 print(f"Falha ao consultar o banco de dados: {bug}")
#             finally:
#                 cursor.close()
#                 conn.close()

    
    # #Classe responsavel por pegar os dados que foram atribuidos e inserir no banco de dados
    # @classmethod
    # def inserirBanco(cls):
    #     conn = conexao_db()
    #     if conn:
    #         cursor = conn.cursor()
    #         try:
               
    #             print('Documento cadastrado')
    #         except Exception as bug:
    #             print(f"Falha ao inserir documento no banco de dados: {bug}")
    #             conn.rollback()
    #         finally:
    #             cursor.close()
    #             conn.close()
    
    # @classmethod
    # def respostaDocumento(cls):
    #     id_resposta = Resposta.id_resposta()
    #     print(f"id_resposta{id_resposta}")
    #     conn = conexao_db()
    #     if conn:
    #         cursor = conn.cursor()
    #         try:
    #             #Aqui estamos associando tabela de pergunta, resposta e documento
    #             #onde o id_reposta tem que ser = id_pergunta
    #             #usamos o retorno da função id_reposta e id_pergunta para configurar
    #             #os parametros do select
    #             cursor.execute  ("""
    #                             SELECT Resposta.id_pergunta, Pergunta.documento FROM Pergunta
	#                             INNER JOIN Resposta ON Pergunta.id_pergunta = Resposta.id_pergunta
	#                             WHERE Pergunta.documento = %s
    #                             """, (1,))
    #             #A partir da tumpla de resultados retornados, pegamos a posição 2
    #             #referente ao atributo documento
    #             documentoAnexo = cursor.fetchall()[0]
    #             #Se atributo for = 0 ele instasia um novo documento     
    #             while documentoAnexo == 1:   
    #                 return cls.inserirBanco()    
    #         except Exception as bug:    
    #             print(f"Falha consultar id_formulario no banco de dados: {bug}")
    #         finally:
    #             cursor.close()
    #             conn.close()

 