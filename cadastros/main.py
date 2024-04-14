from Empresa import Empresa
from Usuario import Usuario
from Resposta import Resposta

def main():
    decisao = input("""
                    Projeto Integrador SAGA - Grupo 2
                    Oque deseja fazer?

                    1 - Cadastrar Empresa
                    2 - Cadastrar Usuario
                    3 - Cadastrar Resposta
                    """
                    )
    
    decisao = int(decisao)

    if decisao == 1:
        Empresa().inserirBanco()
    elif decisao == 2:
        Usuario().inserirBanco()
    elif decisao == 3:
        Resposta().inserirBanco()
    else:
        print("Favor inserir opção valida, 1 a 3.")

if __name__ == "__main__":
    main()
