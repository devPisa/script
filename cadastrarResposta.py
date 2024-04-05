import lorem;
from faker import Faker;

fake = Faker('pt_BR');

def gerarResposta():
    resposta = fake.random_int(1,3);
    if resposta == 1:
        return 'Conforme';
    elif resposta == 2:
        return 'Não Conforme';
    else:
        return 'N/A';

def gerarObservacao():
    observacao = fake.random_int(0,1);
    if observacao == 0:
        return lorem.paragraph()
    else:
        return '';

def cadastrarResposta():
    resposta = gerarResposta();
    observacao = gerarObservacao();
    return(resposta,observacao)