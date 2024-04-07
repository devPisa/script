from faker import Faker
import secrets
import re
from ..database.conexao_db import conexao_db

fake = Faker('pt_BR')
conexao = conexao_db();

class Usuario():
    def gerarNome():
        nome_completo = fake.name()
        if '.' in nome_completo:
            nome_completo = nome_completo.split(' ')[1].strip();
        return nome_completo;

    def gerarEmail(nome:str, sobrenome:str):
        if len(nome) > 0 and len(sobrenome)> 0:
            return f"{nome.split()[0].lower()}{sobrenome.split()[-1].lower()}@bpkgrupo2.com.br";
        return '';

    def formatarTelefone():
        telefone = re.sub(r'D','', fake.phone_number())
        return telefone;

    def formatarCpf():
        cpf = re.sub(r'D','', fake.cpf())
        return cpf;
        
    def cadastrarUsuario(self):
        senha = secrets.token_urlsafe(8);
        nome, sobrenome = self.gerarNome().split(' ', 1);
        cpf = self.formatarCpf();
        telefone = self.formatarTelefone();
        email = self.gerarEmail(nome, sobrenome);
        cidade = fake.city();
        return(senha, nome, sobrenome, cpf, telefone, email, cidade);
    

    def cadastro(self):
        conn = conexao_db();
        if conn:
            cursor = conn.cursor();
            continuar = True;
            while continuar:
                qntd_meta = int(input("Quantos usuarios deseja cadastrar?\n"));
                qntd_atual = 0;
                while qntd_atual <= qntd_meta:
                    values = self.cadastrarUsuario();
                    sql = "INSERT INTO Usuario (senha, nome, sobrenome, cpf, telefone, email, cidade) VALUES (%s, %s, %s, %s, %s, %s, %s,)";
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
  






