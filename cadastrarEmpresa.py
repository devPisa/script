from faker import Faker;
import re;

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

def cadastrarEmpresa():
    fantasia = fake.company();
    razao_social = fantasia;
    cnpj = formatarCnpj();
    email = gerarEmail(fantasia);
    endereco = gerarEndereco();
    telefone = formatarTelefone();
    porte = fake.random_int(1,3);
    atividade = gerarAtividade();
    return(fantasia, razao_social, cnpj, email, endereco, telefone, porte, atividade )