import mysql.connector;
import cadastrarUsuario;

hostname = "localhost:3306";
database = "script_db";
username = "root";
password = "";

try:
    conn = mysql.connector.connect (
    host = hostname,
    user = username,
    password = password,
    database = database 
    )

    if conn.is_connected():
        print ("Conexão realizada com sucesso")
        cursor = conn.cursor()
        sql = "INSERT INTO Usuario (id_usuario, senha, nome, sobrenome, cpf, telefone, email, cidade) VALUES (%d, %s, %s, %s, %s, %s, %s, %s)"
        values = cadastrarUsuario()

        cursor.execute(sql,values)
        conn.commit()

        print("Novo usuário cadastrado!")

        cursor.close()
        conn.close()

    else:
        print("Conexão falhou")
except mysql.connector.Error as bug:
    print(f"Error:{bug}")