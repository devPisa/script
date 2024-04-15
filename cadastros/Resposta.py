import random
from lorem.text import TextLorem
from conexao_db import conexao_db
from faker import Faker
from Formulario import Formulario
from Certificado import Certificado

fake = Faker('pt_BR')
lorem = TextLorem()

class Resposta():
    #A aplicação permite respostas "Conforme" nesse caso sendo 1 e "Não conforme"
    #nesse caso sendo 2, a resposta "N/A" não foi considerada durante a elaboração do
    #scrpit
    @staticmethod
    def gerarResposta():
        return fake.random_int(0,2)

    #Condição para gerar observação no formulario, se = 0, a função retorna um paragrafo
    #lorem, caso contrario retorna uma string vazia
    @staticmethod
    def gerarObservacao():
        if fake.random_int(0,1) == 0:
            return lorem.paragraph()
        return ''
    
    #Função instaciando um novo formulario, e chamando a função para inserir o formulario no banco
    @classmethod
    def id_formulario(cls):
        return Formulario().inserirBanco()
    
    @classmethod
    def pegarId(cls):
        conn = conexao_db()
        cursor = conn.cursor()
        try:
            #Fazendo um select para selecionar um usuario aleatório para atribuir a resposta a ele
            id_usuario = """
                        SELECT Usuario.id_usuario
                        FROM Usuario
                        ORDER BY RAND()
                        LIMIT 1
                        """
            cursor.execute(id_usuario)
            id_usuario = cursor.fetchone()[0]
            print(f"id_usuario = {id_usuario}") # -----------------------------------------------------         
        except Exception as bug:
            print(f"Falha consultar id_usuario no banco de dados: {bug}")
        try:
            #Selecionando todas perguntas existentes no banco
            allPerguntas = """
                        SELECT Pergunta.id_pergunta
                        FROM  Pergunta
                        """
            cursor.execute(allPerguntas)
            id_perguntas = cursor.fetchall()
            
            print(f"id_perguntas = {id_perguntas}") # -----------------------------------------------------PEGOU TODAS AS PERGUNTAS         
        except Exception as bug:
            print(f"Falha consultar id_pergunta no banco de dados: {bug}")
        random.shuffle(id_perguntas)
        
        print(f"id_perguntas = {id_perguntas}") # -----------------------------------------------------
        
        gerarId = []

        #Pegando todas perguntas selecionadas e atribuindo a um vetor que suporte somente
        #as primeiras 15 perguntas
        numPerguntas = min(15, len(id_perguntas)) # ----------------------------------------
    
        print(f"numPerguntas = {numPerguntas}") # -------------------------------------------
        
        objetoFormulario = Formulario()
        novoFomulario = objetoFormulario.inserirBanco()
        id_formulario = Formulario.id_formulario()
        
        print(f"id_formulario = {id_formulario}") #------------------------------------------------
        
        #Mapeando o vetor para retornar uma tumpla de resultado, e concatetando a tumpla
        #o id_usuario, id_pergunta, id_formulario
        # for i in range(numPerguntas):     
        #     id_pergunta = id_perguntas[i][0]     
        #     print(f"id_pergunta dentro do for = {id_pergunta}")  
        gerarId.append((id_usuario, id_perguntas, id_formulario))
        print(gerarId)
        return id_usuario, id_perguntas, id_formulario
    
    
    #Instaciando um novo formulario e chamando a função para inserir no banco
    @classmethod
    def gerarCertificado(cls):
         return Certificado().inserirBanco()
    
    #Classe associada ao banco, responsavel por atribuir todos os dados da tabela

    #Classe responsavel por pegar os dados que foram atribuidos e inserir no banco de dados
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            continuar = True
            while continuar:
                qntd_meta = int(input("Quantos formulários deseja cadastrar?\n"))
                qntd_atual = 0
                while qntd_atual < qntd_meta:
                    observacao = cls.gerarObservacao()
                    id_usuario, id_perguntas, id_formulario = cls.pegarId()
                    id_certificado = cls.gerarCertificado()
                    resposta = cls.gerarResposta()
                    for i in range (qntd_meta):
                        id_pergunta = id_perguntas[i][0]
                        values = (observacao, id_usuario, id_pergunta, id_formulario, id_certificado, resposta)
                        sql = """
                                INSERT INTO Resposta (observacao, id_usuario, id_pergunta, id_formulario, id_certificado, resposta) 
                                VALUES (%s, %s, %s, %s, %s, %s)"""
                        cursor.execute(sql, values)
                        qntd_atual += 1
                        conn.commit()
                        print(f"{qntd_atual} já cadastrados\n")
                decisao = input(f"Deseja continuar? (s/n)")
                if decisao.lower() != 's':
                    continuar = False
            print(f"Cadastro finalizado, {qntd_atual} cadastrados\n") 
            cursor.close()
            conn.close()

    #Classe responsavel por verificar o ultimo id_resposta inserido no banco e retornar
    # para associar a tabela de ceriticado
    @classmethod
    def id_resposta():
        conn = conexao_db()
        cursor = conn.cursor()
        if conn:
            try:
                cursor.execute("""
                                SELECT Resposta.id_pergunta
                                FROM Resposta
                                ORDER BY id_resposta
                                DESC LIMIT 1
                               """)
                id_resposta = cursor.fetchone()[0]
                
                return id_resposta
            except Exception as bug:
                print(f"Falha consultar id_resposta no banco de dados: {bug}")
            finally:
                cursor.close()
                conn.close()
    

    
