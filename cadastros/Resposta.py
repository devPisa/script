from lorem.text import TextLorem;
from faker import Faker;
from Usuario import Usuario;
from Pergunta import Pergunta;
from Formulario import Formulario;
from Certificado import Ceriticado;

fake = Faker('pt_BR');
lorem = TextLorem();

class Resposta():
    def gerarResposta(self):
        resposta = fake.random_int(1,3);
        if resposta == 1:
            return 'Conforme';
        elif resposta == 2:
            return 'Não Conforme';
        else:
            return 'N/A';

    def gerarObservacao(self):
        observacao = fake.random_int(0,1);
        if observacao == 0:
            return lorem.paragraph()
        else:
            return '';

    def cadastrarResposta(self):
        observacao = self.gerarObservacao();
        id_usuario = ##;
        id_pergunta = ##
        id_formulario = ##
        id_certificado = ##
        resposta = self.gerarResposta();

        return(resposta,observacao)