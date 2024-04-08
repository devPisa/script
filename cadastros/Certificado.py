from faker import Faker;
from datetime import datetime;

fake = Faker('pt_BR');

class Certificado():
    #def calcularResultado():
        #resultado
    def gerarData(start_date= datetime.now()):
        date = fake.date_between_dates(date_start=start_date);
        data = (date.day, date.month, (date.year)+1);
        return data;

    def gerarCertificado(self):
        #resultado =
        vencimento = self.gerarData();
        return (resultado, vencimento);
