from faker import Faker;
from conexao_db import conexao_db
from lorem.text import TextLorem

fake = Faker('pt_BR')
lorem = TextLorem()

class Formulario():
   
   #Função para gerar um titulo lorem e definir se o formulario é base ou não
   #para o script ser base ou não não vai influenciar em nada
   #Classe associada ao banco, responsavel por atribuir todos os dados da tabela
    @staticmethod
    def cadastrarFormulario():
        titulo = lorem.sentence()
        print(titulo)
        base = fake.random_int(0, 1)
        return (titulo, base)

    #Classe responsavel por pegar os dados que foram atribuidos e inserir no banco de dados
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                continuar = True
                while continuar:
                    qtdMeta = int(input("Quantos formulários deseja inserir no banco?"))
                    qtdAtual = 0
                    while qtdAtual < qtdMeta:
                        values = cls.cadastrarFormulario()
                        sql =   """
                                INSERT INTO formulario (titulo, base)
                                VALUES (%s, %s)
                                """
                        cursor.execute(sql, values)
                        qtdAtual +=1
                        print(f'Formulario cadastrado')
                        
                        print(f"{qtdAtual} já cadastrados\n")
                        conn.commit()
                        print(values)
                        
                    decisao = input(f"Deseja continuar? (s/n)")
                    if decisao.lower() != 's':
                        continuar = False
                print(f"Cadastro finalizado, {qntdAtual} cadastrados\n")       
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
                