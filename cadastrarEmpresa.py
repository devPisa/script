from faker import Faker
import random
fake = Faker('pt_BR')

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
        return 'Social';
    elif atividade == 2:
        return 'Governamental';
    else:
        return 'Ambiental';
    

def cadastrarEmpresa():
    id_empresa = fake.random_int();
    fantasia = fake.company();
    razao_social = fantasia;
    cnpj = fake.cnpj();
    email = gerarEmail(fantasia);
    endereco = gerarEndereco();
    telefone = fake.phone_number();
    porte = fake.random_int(1,3);
    atividade = gerarAtividade();


    print(f"ID empresa: {id_empresa}");
    print(f"Fantasia: {fantasia}");
    print(f"Razão Sicial: {razao_social}");
    print(f"CNPJ: {cnpj}");
    print(f"E-mail: {email}");
    print(f"Endereço: {endereco}");
    print(f"Telefone: {telefone}");
    print(f"Porte: {porte}");
    print(f"Atividade: {atividade}");

cadastrarEmpresa()