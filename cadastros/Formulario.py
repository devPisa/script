from faker import Faker;
from conexao_db import conexao_db

fake = Faker('pt_BR')

class Formulario():
   
    @staticmethod
    def cadastrarFormulario():
        titulo = fake.random_int()
        base = fake.random_int(0, 1)
        return (titulo, base)

    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                values = cls.cadastrarFormulario()
                sql =   """
                        INSERT INTO Certificado (titulo, base)
                        VALUES (%s, %s)
                        """
                cursor.execute(sql, values)
                conn.commit()
                print(f'Formulario cadastrado')

            except Exception as bug:
                print(f"Falha ao incerir cadastro no banco de dados: {bug}")
                conn.rollback()
            
            finally:
                cursor.close()
                conn.close()
    @classmethod
    def id_formulario(cls):
        conn = conexao_db()
        cursor = conn.cursor()
        if conn:
            try:
                cursor.execute("""
                                SELECT Formulario.id_formulario
                                FROM Formulario
                                ORDER BY id_formulario
                                DESC LIMIT 1
                               """)
                id_formulario = cursor.fetchone()[0]
                
                return id_formulario
            except Exception as bug:
                print(f"Falha consultar id_formulario no banco de dados: {bug}")
            finally:
                cursor.close()
                conn.close()

   
