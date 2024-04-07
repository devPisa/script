from faker import Faker;
import re;
from ..database.conexao_db import conexao_db

fake = Faker('pt_BR')

class Empresa():
    def gerarEmail(fantasia:str):
        if len(fantasia) > 0:
            return f"{fantasia.split()[0].lower()}@bpkgrupo2.com.br";
        return '';

    def gerarEndereco():
        endereco = fake.address();
        if ',' in endereco:
            endereco = endereco.split(',')[0].strip(); 
        elif '\n' in endereco:
            endereco = endereco.split('\n')[0].strip;
        return endereco ;

    def gerarAtividade():
        atividade = fake.random_int(1, 3);
        if atividade == 1:
            return 'Industrial';
        elif atividade == 2:
            return 'Social';
        else:
            return 'Serviço';

    def formatarTelefone():
        telefone = re.sub(r'D','', fake.phone_number())
        return telefone;

    def formatarCnpj():
        cnpj = re.sub(r'D','',fake.cnpj());
        return cnpj;    

    def cadastrarEmpresa(self):
        fantasia = fake.company();
        razao_social = fantasia;
        cnpj = self.formatarCnpj();
        email = self.gerarEmail(fantasia);
        endereco = self.gerarEndereco();
        telefone = self.formatarTelefone();
        porte = fake.random_int(1,3);
        atividade = self.gerarAtividade();
        return(fantasia, razao_social, cnpj, email, endereco, telefone, porte, atividade )
    
    def cadastro(self):
        conn = conexao_db();
        if conn:
            cursor = conn.cursor();
            continuar = True;
            while continuar:
                qntd_meta = int(input("Quantas empresas deseja cadastrar?\n"));
                qntd_atual = 0;
                while qntd_atual <= qntd_meta:
                    values = self.cadastrarEmpresa();
                    sql = "INSERT INTO Empresa (fantasia, razao_social, cnpj, email, endereco, telefone, porte, atividade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)";
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
  