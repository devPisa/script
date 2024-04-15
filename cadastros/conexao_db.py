import mysql.connector

def conexao_db():
    hostname = "localhost"
    database = "script_db"
    username = "root"
    password = ""

    try:
        conn = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )

        if conn.is_connected():
            return conn
        else:
            return None

    except mysql.connector.Error as bug:
        print(f"Erro ao conectar:{bug}")
        return None
