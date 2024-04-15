from Empresa import Empresa
from Usuario import Usuario
from Resposta import Resposta
from Pergunta import Pergunta
from Certificado import Certificado
from Formulario import Formulario
from FormularioPergunta import formularioPergunta
from Documento import Documento

def main():
    decisao = input("""
                    Projeto Integrador SAGA - Grupo 2
                    Oque deseja fazer?

                    1 - Cadastrar Empresa
                    2 - Cadastrar Usuario
                    3 - Cadastrar Resposta
                    4 - Cadastrar Pergunta
                    5 - Cadastrar Formulario
                    6 - Cadastrar nnCertificado
                    7 - Relacionar Pergunta ao Formulário
                    8 - Inserir Link de Documento
                    """
                    )
    
    decisao = int(decisao)

    
    if decisao == 1:
        Empresa().inserirBanco()
    elif decisao == 2:
        Usuario().inserirBanco()
    elif decisao == 3:
        Resposta().inserirBanco()
    elif decisao == 4:
        Pergunta().inserirBanco()
    elif decisao == 5:
        Formulario().inserirBanco()
    elif decisao == 6:
        Certificado().inserirBanco()
    elif decisao == 7: 
        formularioPergunta().inserirBanco()
    elif decisao == 8:
        Documento().respostaDocumento()
    else:
        print("Favor inserir opção valida, 1 a 3.")

if __name__ == "__main__":
    main()