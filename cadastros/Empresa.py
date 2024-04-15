from faker import Faker
import re
from conexao_db import conexao_db

fake = Faker('pt_BR')

class Empresa():
    #Função gera um e-mail a partir do nome e sobrenome do usuario
    #Ela concatena a primeira letra do primeiro nome com o ultimo nome
    #Ainda adiciona o dominio bpkgrupo2.com e tranforma tudo em lower(minusculo)
    @staticmethod
    def gerarEmail(fantasia:str):
        if len(fantasia) > 0:
            return f"{fantasia.split()[0].lower()}@bpkgrupo2.com.br"
        return ''

    #Função responsavel por gerar endereço, ela atribui um endereço e elimina tudo
    #que existe depois da virgula e ainda faz uma verificação se o endereço tem mais
    #de uma linha, se sim, tambem elimina
    @staticmethod
    def gerarEndereco():
        endereco = fake.address()
        if ',' in endereco:
            endereco = endereco.split(',')[0].strip() 
        elif '\n' in endereco:
            endereco = endereco.split('\n')[0].strip()
            return endereco

    #Função gerar atividade, faz um random de 1 á 3 e atribuir a atividade
    #aleatoriamente de acordo com o numero
    @staticmethod
    def gerarAtividade():
        atividade = fake.random_int(1, 3)
        if atividade == 1:
            return 'Industrial'
        elif atividade == 2:
            return 'Social'
        else:
            return 'Serviço'

    #Função forma o telefone, a formatação elimina espaços e caractenres especiais
    @staticmethod
    def formatarTelefone():
        telefone = re.sub(r'\D','', fake.phone_number())
        return telefone
    
    #Função forma o CNPJ, a formatação elimina espaços e caracteres especiais
    @staticmethod
    def formatarCnpj():
        cnpj = re.sub(r'\D','',fake.cnpj())
        return cnpj    

    #Classe associada ao banco, responsavel por atribuir todos os dados da tabela
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
    
     #Classe responsavel por pegar os dados que foram atribuidos e inserir no banco de dados
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
                    while qntdAtual < qntdMeta:
                        values = cls.cadastrarEmpresa()
                        sql =   """
                                INSERT INTO Empresa (fantasia, razao_social, cnpj, email, endereco, telefone, porte, atividade) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                """
                        cursor.execute(sql, values)
                        qntdAtual += 1
                        
                        print(f"{qntdAtual} já cadastrados\n")
                        conn.commit()
                        print(values)
                    decisao = input(f"Deseja continuar? (s/n)")
                    if decisao.lower() != 's':
                        continuar = False
                print(f"Cadastro finalizado, {qntdAtual} cadastrados\n")

            except Exception as bug:
                print(f"Falha ao incerir cadastro no banco de dados: {bug}");
                conn.rollback();
            
            finally:
                cursor.close()
                conn.close()
  