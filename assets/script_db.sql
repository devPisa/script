CREATE DATABASE script_db;

USE script_db;

-- SQL ADAPTADO PARA RODAR COM O SCRIPT PYTHON

CREATE TABLE    Usuario (
                id_usuario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                senha VARCHAR(45) NOT NULL,
                nome VARCHAR(45) NOT NULL,
                sobrenome VARCHAR(45) NOT NULL,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                telefone VARCHAR(20) NOT NULL,
                email VARCHAR(45) NOT NULL,
                cidade VARCHAR(45)
                );

CREATE TABLE    Empresa (
                id_empresa INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                fantasia VARCHAR(45) NOT NULL,
                razao_social VARCHAR(45) NOT NULL,
                cnpj VARCHAR(14) NOT NULL,
                email VARCHAR(45) NOT NULL,
                endereco VARCHAR(150),
                telefone VARCHAR(20),
                porte SMALLINT NOT NULL,
                atividade VARCHAR(30) NOT NULL
                );

CREATE TABLE    Usuario_empresa (
                id_usuario INT NOT NULL,
                id_empresa INT NOT NULL,
                PRIMARY KEY (id_usuario, id_empresa),
                FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
                FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa)
                );

CREATE TABLE    Formulario (
                id_formulario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                titulo VARCHAR(45),
                base TINYINT
                );

CREATE TABLE    Pergunta (
                id_pergunta INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                titulo VARCHAR(255),
                documento TINYINT NOT NULL
                );

CREATE TABLE    Formulario_pergunta (
                id_formulario INT,
                id_pergunta INT,
                PRIMARY KEY (id_formulario, id_pergunta),
                FOREIGN KEY (id_formulario) REFERENCES Formulario(id_formulario),
                FOREIGN KEY (id_pergunta) REFERENCES Pergunta(id_pergunta)
                );

CREATE TABLE    Certificado (
                id_certificado INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                resultado DOUBLE,
                id_formulario INT NOT NULL,
                id_empresa INT NOT NULL,
                vencimento DATE,
                FOREIGN KEY (id_formulario) REFERENCES Formulario(id_formulario),
                FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa)
                );

CREATE TABLE    Resposta (
                id_resposta INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                observacao TEXT,
                id_usuario INT NOT NULL,
                id_pergunta INT NOT NULL,
                id_formulario INT NOT NULL,
                id_certificado INT NOT NULL,
                resposta VARCHAR(10) NOT NULL,
                FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
                FOREIGN KEY (id_pergunta) REFERENCES Pergunta(id_pergunta),
                FOREIGN KEY (id_formulario) REFERENCES Formulario(id_formulario),
                FOREIGN KEY (id_certificado) REFERENCES Certificado(id_certificado)
                );

CREATE TABLE    Documento (
                id_documento INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                url_documento VARCHAR(2049) NOT NULL,
                id_resposta INT NOT NULL,
                validado TINYINT,
                FOREIGN KEY (id_resposta) REFERENCES Resposta(id_resposta)
                );
