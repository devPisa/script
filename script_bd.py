import mysql.connect
from faker import Faker
hostname = "localhost:3306"
database = "script_db"
username = "root"
password = ""

try:
    conn = mysql.connector.connect(
        host = hostname,
        user = username,
        password = password,
        database = database
    )

if conn.is_connected():
    print ("Conexão realizada com sucesso")

    cursor = conn.cursor()

    sql = "INSERT INTO Usuario id_usuario, senha, nome, sobrenome, cpf, telefone, email, cidade) VALUES (%d, %s, %s, %s, %s, %s, %s, %s)"
    values = ("")