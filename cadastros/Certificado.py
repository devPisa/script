from faker import Faker
from datetime import datetime
from Formulario import Formulario
from conexao_db import conexao_db

fake = Faker('pt_BR')

class Certificado():

    @classmethod 
    def pegarId(cls):
        id_formulario = Formulario.id_formulario()
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                #Aqui estamos fazendo um select na tabela empresa e sortenado uma 
                #empresa aleatoria
                id_empresaQuery =   """
                                    SELECT Empresa.id_empresa
                                    FROM Empresa
                                    ORDER BY RAND()
                                    LIMIT 1
                                    """
                cursor.execute(id_empresaQuery)
                id_empresa = cursor.fetchone()[0]
                return (id_formulario, id_empresa)
            except Exception as bug:
                print(f"Falha consultar id_empresa no banco de dados: {bug}")
            finally:
                cursor.close()
                conn.close()

    @classmethod
    def calcularResultado(cls):
        id_formulario = Formulario.id_formulario()
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                #Consultando o banco de dados e fazendo a media dos dados da resposta
                cursor.execute  ("""
                                SELECT AVG(Resposta.resposta) AS mediaRespostas
                                FROM Resposta   
                                INNER JOIN Formulario ON Resposta.id_formulario = Formulario.id_formulario
                                Where Resposta.id_formulario = Formulario.%s
                                """, (id_formulario,))
                mediaResposta = cursor.fetchone()[0]
                calculoResultado = (mediaResposta) * 100
                #regra de negocio para calcular a media
                if calculoResultado < 74:
                    resultadoMedia = 'Reprovado'
                elif 75 <= calculoResultado <= 85:
                    resultadoMedia = 'Bronze'
                elif 86 <= calculoResultado <= 94:
                    resultadoMedia = 'Prata'
                else:
                    resultadoMedia = 'Ouro'
                return resultadoMedia
            
            except Exception as bug:
                print(f"Falha ao localizar dados: {bug}")
                return None
            finally:
                cursor.close()
                conn.close()

    #Função pegar pegar a data atual e somar 1 ano, para atribuir a validade do formulario
    @staticmethod       
    def gerarData(start_date= datetime.now()):
        date = fake.date_between_dates(date_start=start_date)
        data = (date.day, date.month, (date.year)+1)
        return data

    #Classe associada ao banco, responsavel por atribuir todos os dados da tabela
    @classmethod
    def gerarCertificado(cls):
        resultado = cls.calcularResultado()
        id_formulario, id_empresa = cls.pegarId()
        vencimento = cls.gerarData()
        return (resultado, id_formulario, id_empresa, vencimento)

    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()

        if conn:
            cursor= conn.cursor()
            
            try:
                values = cls.gerarCertificado()
                sql =   """
                        INSERT INTO Certificado (resultado, id_formulario, id_empresa, vencimento)
                        VALUES (%s, %s, %s, %s)
                        """
                cursor.execute(sql, values)
                print(f'Certificado cadastrado, resultado: {values[0]}')
                conn.commit()
                cursor.execute("""
                                SELECT LAST_INSERT_ID()
                               """)
                id_certificado = cursor.fetchone()[0]
                
                return id_certificado

            except Exception as bug:
                print(f"Falha ao incerir cadastro no banco de dados: {bug}")
                conn.rollback()
            
            finally:
                cursor.close()
                conn.close()



