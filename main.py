from cadastros.Empresa import Empresa
from cadastros.Usuario import Usuario
from cadastros.Resposta import Resposta

def main():
    while True:
        decisao = int(input("""
                            Projeto Integrador SAGA - Grupo 2
                            Oque deseja fazer?
                            """
                            ))
        print("""
                1 - Cadastrar Empresa
                2 - Cadastrar Usuario
                3 - Cadastrar Resposta
                """)
        if decisao == 1:
            Empresa().inserirBanco()
            break
        elif decisao == 2:
            Usuario().inserirBanco()
            break
        elif decisao == 3:
            Resposta().inserirBanco()
            break
        else:
            print("Favor inserir opção valida, 1 a 3.")
    
if __name__ == "__main__":
    main()