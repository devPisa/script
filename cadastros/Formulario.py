from faker import Faker
from ..database.conexao_db import conexao_db

fake = Faker('pt_BR');

class Formulario():
    def tipoFormulario():
        tipoFormulario = fake.random_int(1,3);
        if tipoFormulario == 1:
            return 'Social';
        elif tipoFormulario == 2:
            return 'Ambiental';
        else :
            return 'Governamental';

    def cadastrarFormulario(self):
        titulo = self.tipoFormulario();
        base = fake.random_int(0, 1);
        return (titulo);

    def cadastro(self):
        conn = conexao_db();
        if conn:
            cursor = conn.cursor();
            continuar = True;
            while continuar:
                qntd_meta = int(input("Quantos formulários deseja cadastrar?\n"));
                qntd_atual = 0;
                while qntd_atual <= qntd_meta:
                    values = self.cadastrarFormulario();
                    sql = "INSERT INTO Formulario (titulo, base) VALUES (%s)";
                    cursor.execute(sql, values);
                    qntd_atual += 1;
                    print(f"{qntd_atual} já cadastrados\n");
                decisao = input(f"Deseja continuar? (s/n)");
                if decisao.lower() != 's':
                    continuar = False;
            print(f"Cadastro finalizado, {qntd_atual} cadastrados\n")
            conn.commit();
            cursor.close();
            conn.close()