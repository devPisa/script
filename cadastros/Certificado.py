from faker import Faker
from datetime import datetime
from Resposta import Resposta
from Formulario import Formulario
from Empresa import Empresa
from database.conexao_db import conexao_db

fake = Faker('pt_BR')

class Certificado():
    
    @classmethod
    def calcularResultado(cls):
        objetoReposta = Resposta()
        calculoResultado = objetoReposta.resposta()
        qntdRespostas = len(Resposta)
        qntdAcerto = sum(Resposta[3]
                         for Resposta in Resposta)
        calculoResultado = (qntdAcerto/qntdRespostas) * 100

        if calculoResultado < 74:
            resultadoMedia = 'Reprovado'
        elif 75 <= calculoResultado <= 85:
            resultadoMedia = 'Bronze'
        elif 86 <= calculoResultado <= 94:
            resultadoMedia = 'Prata'
        else:
            resultadoMedia = 'Ouro'
        return resultadoMedia

    @staticmethod       
    def gerarData(start_date= datetime.now()):
        date = fake.date_between_dates(date_start=start_date);
        data = (date.day, date.month, (date.year)+1);
        return data

    @staticmethod #precisa verificar, pegar a função de resposta
    def pegarId():
        objetoFormulario = Formulario()
        id_formulario = objetoFormulario.inserirBanco()
        objetoEmpresa = Empresa() #pegar a logica de resposta
        id_empresa = objetoEmpresa.inserirBanco()
        return (id_formulario, id_empresa)

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



