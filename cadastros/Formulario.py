from faker import Faker;
from conexao_db import conexao_db
from lorem.text import TextLorem

fake = Faker('pt_BR')
lorem = TextLorem()

class formulario():
   
   #Função para gerar um titulo lorem e definir se o formulario é base ou não
   #para o script ser base ou não não vai influenciar em nada
   #Classe associada ao banco, responsavel por atribuir todos os dados da tabela
    @staticmethod
    def cadastrarFormulario():
        titulo = lorem.sentence()
        base = fake.random_int(0, 1)
        return (titulo, base)

    #Classe responsavel por pegar os dados que foram atribuidos e inserir no banco de dados
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                values = cls.cadastrarFormulario()
                sql =   """
                        INSERT INTO formulario (titulo, base)
                        VALUES (%s, %s)
                        """
                cursor.execute(sql, values)
                conn.commit()     
            except Exception as bug:
                print(f"Falha ao inserir cadastro no banco de dados: {bug}")
                conn.rollback()  
            finally:
                cursor.close()
                conn.close()

    #Classe responsavel por recuperar o ultimo id_formulario inserido e usar para
    #associar a tabela resposta                  
    @classmethod
    def id_formulario(cls):
        conn = conexao_db()
        cursor = conn.cursor()
        if conn:
            try:
                cursor.execute("""
                                SELECT Formulario.id_formulario
                                FROM Formulario
                                ORDER BY rand()
                                LIMIT 1
                               """)
                id_formulario = cursor.fetchone()[0]
                return id_formulario
            except Exception as bug:
                print(f"Falha consultar id_formulario no banco de dados: {bug}")
            finally:
                cursor.close()
                conn.close()
                