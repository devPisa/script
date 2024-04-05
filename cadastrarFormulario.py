from faker import Faker

fake = Faker('pt_BR');

def tipoFormulario():
    tipoFormulario = fake.random_int(1,3);
    if tipoFormulario == 1:
        return 'Social';
    elif tipoFormulario == 2:
        return 'Ambiental';
    else :
        return 'Governamental';

def cadastrarFormulario():
    titulo = tipoFormulario();
    return (titulo);