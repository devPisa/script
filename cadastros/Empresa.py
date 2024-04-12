from faker import Faker
import re
from conexao_db import conexao_db

fake = Faker('pt_BR')

class Empresa():
    @staticmethod
    def gerarEmail(fantasia:str):
        if len(fantasia) > 0:
            return f"{fantasia.split()[0].lower()}@bpkgrupo2.com.br"
        return ''

    @staticmethod
    def gerarEndereco():
        endereco = fake.address()
        if ',' in endereco:
            endereco = endereco.split(',')[0].strip() 
        elif '\n' in endereco:
            endereco = endereco.split('\n')[0].strip;
        return endereco

    @staticmethod
    def gerarAtividade():
        atividade = fake.random_int(1, 3)
        if atividade == 1:
            return 'Industrial'
        elif atividade == 2:
            return 'Social'
        else:
            return 'Serviço'

    @staticmethod
    def formatarTelefone():
        telefone = re.sub(r'D','', fake.phone_number())
        return telefone

    @staticmethod
    def formatarCnpj():
        cnpj = re.sub(r'D','',fake.cnpj())
        return cnpj    

    @classmethod
    def cadastrarEmpresa(cls):
        fantasia = fake.company()
        razao_social = fantasia
        cnpj = cls.formatarCnpj()
        email = cls.gerarEmail(fantasia)
        endereco = cls.gerarEndereco()
        telefone = cls.formatarTelefone()
        porte = fake.random_int(1,3)
        atividade = cls.gerarAtividade()
        return(fantasia, razao_social, cnpj, email, endereco, telefone, porte, atividade)
    
    @classmethod
    def inserirBanco(cls):
        conn = conexao_db()
        
        if conn:
            cursor = conn.cursor()

            try:

                continuar = True
                while continuar:
                    qntdMeta = int(input("Quantas empresas deseja cadastrar?\n"))
                    qntdAtual = 0
                    while qntdAtual <= qntdMeta:
                        values = cls.cadastrarEmpresa()
                        sql =   """
                                INSERT INTO Empresa (fantasia, razao_social, cnpj, email, endereco, telefone, porte, atividade) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                """
                        cursor.execute(sql, values)
                        qntdAtual += 1
                        print(f"{qntdAtual} já cadastrados\n")
                    decisao = input(f"Deseja continuar? (s/n)")
                    if decisao.lower() != 's':
                        continuar = False
                print(f"Cadastro finalizado, {qntdAtual} cadastrados\n")
                conn.commit()

            except Exception as bug:
                print(f"Falha ao incerir cadastro no banco de dados: {bug}");
                conn.rollback();
            
            finally:
                cursor.close()
                conn.close()
  