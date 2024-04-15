import random
from lorem.text import TextLorem
from conexao_db import conexao_db
from faker import Faker
from Formulario import Formulario
from Certificado import Certificado

class Teste():
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
        for i in range(numPerguntas):
            
            id_pergunta = id_perguntas[i][0]
            
            print(f"id_pergunta dentro do for = {id_pergunta}")
            
            gerarId.append((id_usuario, id_pergunta, id_formulario))
            
        return gerarId


