from formulario import formulario
from pergunta import pergunta
from conexao_db import conexao_db

class formularioPergunta:
    
    @classmethod
    def pegarId(cls):
        id_formulario = formulario.id_formulario()
        id_pergunta = pergunta.id_pergunta()
        return (id_formulario, id_pergunta)
    
    #Classe responsavel por pegar os dados que foram atribuidos e inserir no banco de dados
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                values = cls.pegarId()
                sql=    ("""
                        INSERT INTO formulario_pergunta (id_formulario, id_pergunta)
                        VALUES (%s, %s)
                        """)    
                cursor.execute(sql, values)
                conn.commit()
            except Exception as bug:
                  print(f"Falha ao cadastrar relacionamento formulario_pergunta no banco de dados: {bug}")
            finally:
                cursor.close()
                conn.close()