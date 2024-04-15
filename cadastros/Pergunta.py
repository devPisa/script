from faker import Faker
from conexao_db import conexao_db
import lorem;

fake = Faker('pt_BR');

class pergunta:

    #Classe associada ao banco, responsavel por atribuir todos os dados da tabela
    @classmethod
    def cadastrarPergunta(cls):
        pergunta =lorem.sentence()
        documento = fake.random_int(0,1)
        return(pergunta, documento)
    
    #Classe responsavel por pegar os dados que foram atribuidos e inserir no banco de dados
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                values = cls.cadastrarPergunta()
                sql =   """
                        INSERT INTO Pergunta(pergunta, documento)
                        VALUES (%s, %s)
                        """
                cursor.execute(sql, values)
                conn.commit()
            except Exception as bug:
                print(f"Falha ao inserir cadastro no banco de dados: {bug}");
                conn.rollback();
            finally:
                cursor.close()
                conn.close()

    #Classe responsavel por recuperar o ultimo id_pergunta inserido e usar para
    #associar a tabela resposta
    @classmethod
    def id_pergunta(cls):
        conn = conexao_db()
        cursor = conn.cursor()
        if conn:
            try:
                cursor.execute("""
                                SELECT Pergunta.id_pergunta
                                FROM Pergunta
                                ORDER BY rand()
                                LIMIT 1
                               """)
                id_pergunta = cursor.fetchone()[0]
                return id_pergunta
            except Exception as bug:
                print(f"Falha consultar id_pergunta no banco de dados: {bug}")
            finally:
                cursor.close()
                conn.close()    

