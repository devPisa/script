from faker import Faker
import secrets
import re
from conexao_db import conexao_db

fake = Faker('pt_BR')
conexao = conexao_db()

class Usuario():
    
    @staticmethod
    def gerarNome():
        nome_completo = fake.name()
        if '.' in nome_completo:
            nome_completo = nome_completo.split(' ')[1].strip()
        return nome_completo

    @staticmethod
    def gerarEmail(nome:str, sobrenome:str):
        if len(nome) > 0 and len(sobrenome)> 0:
            return f"{nome.split()[0].lower()}{sobrenome.split()[-1].lower()}@bpkgrupo2.com.br"
        return ''
    
    @staticmethod
    def formatarTelefone():
        telefone = re.sub(r'D','', fake.phone_number())
        return telefone

    @staticmethod
    def formatarCpf():
        cpf = re.sub(r'D','', fake.cpf())
        return cpf;

    @classmethod      
    def cadastrarUsuario(cls):
        senha = secrets.token_urlsafe(8)
        nome, sobrenome = cls.gerarNome().split(' ', 1)
        cpf = cls.formatarCpf()
        telefone = cls.formatarTelefone()
        email = cls.gerarEmail(nome, sobrenome)
        cidade = fake.city()
        return(senha, nome, sobrenome, cpf, telefone, email, cidade)
    
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        if conn:
            cursor = conn.cursor()
            try:
                continuar = True
                while continuar:
                    qntd_meta = int(input("Quantos usuarios deseja cadastrar?\n"))
                    qntd_atual = 0;
                    while qntd_atual <= qntd_meta:
                        values = cls.cadastrarUsuario()
                        sql =   """
                                INSERT INTO Usuario (senha, nome, sobrenome, cpf, telefone, email, cidade) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s,)
                                """
                        cursor.execute(sql, values)
                        qntd_atual += 1
                        print(f"{qntd_atual} já cadastrados\n")
                    decisao = input(f"Deseja continuar? (s/n)")
                    if decisao.lower() != 's':
                        continuar = False
                print(f"Cadastro finalizado, {qntd_atual} cadastrados\n")
                conn.commit()
            except Exception as bug:
                print(f"Falha ao incerir cadastro no banco de dados: {bug}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
  






