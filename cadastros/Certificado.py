from faker import Faker;
from datetime import datetime;
from Resposta import Resposta;
from ..database.conexao_db import cursor, conexao_db;

fake = Faker('pt_BR');

class Certificado():
    @staticmethod
    def calcularResultado():
        objeto_reposta = Resposta();
        calculoResultado = objeto_reposta.resposta();
        if calculoResultado < 74:
            resultadoMedia = 'Reprovado'
        elif 75 <= calculoResultado <= 85:
            resultadoMedia = 'Bronze'
        elif 86 <= calculoResultado <= 94:
            resultadoMedia = 'Prata'
        else:
            resultadoMedia = 'Ouro'
        return resultadoMedia;

    @staticmethod       
    def gerarData(start_date= datetime.now()):
        date = fake.date_between_dates(date_start=start_date);
        data = (date.day, date.month, (date.year)+1);
        return data;

    @staticmethod
    def pegarId(conn):
        select = """
                SELECT formulario.id_formulario, empresa.id_empresa
                FROM formulario
                INNER JOIN certificado ON formulario.id_formulario = certificado.id_formulario
                INNER JOIN empresa ON certificado.id_empresa = empresa.id_empresa
                """
        cursor.execute(select);
        returnSelect = cursor.fetchone();

        if returnSelect:
            id_formulario, id_empresa = returnSelect
            return id_formulario, id_empresa
        else:
            return None;

    @classmethod
    def gerarCertificado(cls):
        resultado = cls.calcularResultado();
        id_formulario, id_empresa = cls.pegarId(cursor);
        vencimento = cls.gerarData();
        return (resultado, id_formulario, id_empresa, vencimento);

    @classmethod
    def inserirBanco(cls):
        conn = conexao_db();
        if conn:
            cursor= conn.cursor();
            try:
                values = cls.gerarCertificado();
                sql = "INSERT INTO Certificado (resultado, id_formulario, id_empresa, vencimento)"
                cursor.execute(sql, values);
                print(f'Certificado cadastrado, resultado: {values[0]}');
                conn.commit();

            except Exception as bug:
                print(f"Falha ao incerir cadastro no banco de dados: {bug}");
                conn.rollback();
            
            finally:
                cursor.close();
                conn.close();



