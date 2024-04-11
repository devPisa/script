import random
from lorem.text import TextLorem
from database.conexao_db import conexao_db
from faker import Faker
from Formulario import Formulario
from Certificado import Certificado
from Documento import Documento


fake = Faker('pt_BR')
lorem = TextLorem();

class Resposta():

    @staticmethod
    def gerarResposta():
        return fake.random_int(1,3) == 1

    @staticmethod
    def gerarObservacao():
        if fake.random_int(0,1) == 0:
            return lorem.paragraph()
        return ''

    @classmethod
    def id_formulario(cls):
        return Formulario().inserirBanco()
    
    @classmethod
    def pegarId(cls):
        conn = conexao_db()
        cursor = conn.cursor()
        try:
            id_usuario = """
                        SELECT usuario.id_usuario
                        FROM usuario
                        ORDER BY RAND()
                        LIMIT 1
                        """
            cursor.execute(id_usuario)
            id_usuario = cursor.fetchone()[0]
        except Exception as bug:
            print(f"Falha consultar id_usuario no banco de dados: {bug}")
        try:
            allPerguntas = """
                        SELECT pergunta.id_pergunta
                        FROM  pergunta
                        """
            cursor.execute(allPerguntas)
            id_perguntas = cursor.fetchall()
        except Exception as bug:
            print(f"Falha consultar id_pergunta no banco de dados: {bug}")

        random.shuffle(id_perguntas)

        gerarId = []

        numPerguntas = min(15, len(id_perguntas))
        
        id_formulario = cls.id_formulario()

        for i in range(numPerguntas):
            id_pergunta = id_perguntas[i][0]
            gerarId.append((id_usuario, id_pergunta, id_formulario))
        return gerarId
    
    @classmethod
    def gerarCertificado(cls):
         return Certificado().inserirBanco()
    
    @classmethod
    def respostaDocumento(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()

            try:
                id_pergunta, existeDocumento = cls.gerarId()[1]
                if existeDocumento == 0:
                    objetoDocumento = Documento()
                    anexarDocumento = objetoDocumento.gerarDocumento()
                    sql =   """
                            UPDATE pergunta
                            SET documento = %s
                            WHERE id_pergunta = %s
                            """
                    cursor.execute(sql, (id_pergunta,anexarDocumento))
                    conn.commit()
                    print(f"Documento cadastrado com sucesso") 

            except Exception as bug:
                print(f"Falha ao inserir documento no banco de dados: {bug}")
                conn.rollback();
            finally:
                cursor.close()
                conn.close()

    @classmethod
    def cadastrarResposta(cls):
        observacao = cls.gerarObservacao();
        id_usuario, id_pergunta, id_formulario = cls.pegarId();
        id_certificado = cls.gerarCerfiticado();
        resposta = cls.gerarResposta();
        return(observacao, id_usuario, id_pergunta, id_formulario, id_certificado, resposta);

    @classmethod
    def inserirBanco(cls):
        conn = conexao_db();
        if conn:
            cursor = conn.cursor();
            continuar = True;
            while continuar:
                qntd_meta = int(input("Quantos formulários deseja cadastrar?\n"));
                qntd_atual = 0;
                while qntd_atual <= qntd_meta:
                    values = cls.cadastrarResposta();
                    sql = """
                            INSERT INTO Resposta (observacao, id_usuario, id_pergunta, id_formulario, id_certificado, resposta) 
                            VALUES (%s, %s, %s, %s, %s, %s)""";
                    cursor.execute(sql, values);
                    qntd_atual += 1;
                    print(f"{qntd_atual} já cadastrados\n");
                decisao = input(f"Deseja continuar? (s/n)");
                if decisao.lower() != 's':
                    continuar = False;
            print(f"Cadastro finalizado, {qntd_atual} cadastrados\n")
            conn.commit();
            cursor.close();
            conn.close()
    
