from faker import Faker;
from datetime import datetime

fake = Faker('pt_BR');

#def calcularResultado():
    #resultado
def gerarData(start_date= datetime.now()):
    date = fake.date_between_dates(date_start=start_date);
    data = (date.day, date.month, (date.year)+1);
    return data;

def gerarCertificado():
    #resultado =
    vencimento = gerarData();
    print(f'{vencimento}')
gerarCertificado();