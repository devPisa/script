from Formulario import Formulario
from Pergunta import Pergunta
from conexao_db import conexao_db

class formularioPergunta:
    
    @classmethod
    def pegarId(cls):
        id_formulario = Formulario.id_formulario()
        print(id_formulario)
        id_pergunta = Pergunta.id_pergunta()
        print(id_pergunta)
        
        return (id_formulario, id_pergunta)
    
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                values = cls.pegarId()
                print(values)
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