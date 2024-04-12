from Empresa import Empresa
from Usuario import Usuario
from Resposta import Resposta
from conexao_db import conexao_db
def main():
    conn = conexao_db()
    if conn:
        while True:
            decisao = int(input("""
                                Projeto Integrador SAGA - Grupo 2
                                Oque deseja fazer?

                                1 - Cadastrar Empresa
                                2 - Cadastrar Usuario
                                3 - Cadastrar Resposta
                                """
                                ))
            print()
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
    
    else:
        print("Falha ao conectar ao banco")
if __name__ == "__main__":
    main()