from faker import Faker
import secrets
import re

fake = Faker('pt_BR')

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
    
def cadastrarUsuario():
    senha = secrets.token_urlsafe(8);
    nome, sobrenome = gerarNome().split(' ', 1);
    cpf = formatarCpf();
    telefone = formatarTelefone();
    email = gerarEmail(nome, sobrenome);
    cidade = fake.city();
    
    return(senha, nome, sobrenome, cpf, telefone, email, cidade);

