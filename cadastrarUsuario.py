from faker import Faker
import secrets
import random

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
    
def cadastrarUsuario():
    id_usuario = fake.random_int();
    senha = secrets.token_urlsafe(8);
    nome, sobrenome = gerarNome().split(' ', 1);
    cpf = fake.cpf();
    phone = fake.phone_number();
    email = gerarEmail(nome, sobrenome);
    cidade = fake.city();
    print(f"ID de Usuario: {id_usuario}")
    print(f"Senha: {senha}")
    print(f"Nome: {nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"CPF: {cpf}")
    print(f"Telefone: {phone}")
    print(f"E-mail: {email}")
    print(f"Cidade: {cidade}")
cadastrarUsuario()
