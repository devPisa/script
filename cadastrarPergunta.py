from faker import Faker;
import lorem;

fake = Faker('pt_BR');

def cadastrarPergunta():
    pergunta =lorem.sentence();
    documento = fake.random_int(0,1);
    return(pergunta, documento)
