from faker import Faker
import secrets
import re
from conexao_db import conexao_db

fake = Faker('pt_BR')
conexao = conexao_db()

class usuario():
    #Função gera um nome aleatório, como a lib faker gera nome com prefixo (Dr. Sr.)
    #foi feita uma adptação para eliminar o prefixo
    @staticmethod
    def gerarNome(): 
        nome_completo = fake.name()
        if '.' in nome_completo:
            partes_nome = nome_completo.split(' ')
            nome_completo = ' '.join(partes_nome[1:])
        return nome_completo

    @staticmethod
    def gerarEmail(nome:str, sobrenome:str):
        if len(nome) > 0 and len(sobrenome)> 0:
            return f"{nome.split()[0].lower()}{sobrenome.split()[-1].lower()}@bpkgrupo2.com.br"
        return ''
    
    #Função forma o telefone, a formatação elimina espaços e caracteres especiais
    @staticmethod
    def formatarTelefone():
        telefone = re.sub(r'\D','', fake.phone_number())
        return telefone

    #Função forma o CPF, a formatação elimina espaços e caracteres especiais
    @staticmethod
    def formatarCpf():
        cpf = re.sub(r'\D','', fake.cpf())
        return cpf

    #Classe associada ao banco, responsavel por atribuir todos os dados da tabela
    @classmethod      
    def cadastrarUsuario(cls):
        senha = secrets.token_urlsafe(8)
        nome, sobrenome = cls.gerarNome().split(' ', 1)
        cpf = cls.formatarCpf()
        telefone = cls.formatarTelefone()
        email = cls.gerarEmail(nome, sobrenome)
        cidade = fake.city()
        return(senha, nome, sobrenome, cpf, telefone, email, cidade)
    
    #Classe responsavel por pegar os dados que foram atribuidos e inserir no banco de dados
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                values = cls.cadastrarUsuario()
                sql =   """
                        INSERT INTO Usuario (senha, nome, sobrenome, cpf, telefone, email, cidade) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """
                cursor.execute(sql, values)
                conn.commit()
            except Exception as bug:
                print(f"Falha ao inserir cadastro no banco de dados: {bug}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
  






