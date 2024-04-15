from empresa import empresa
from usuario import usuario
from resposta import resposta
from pergunta import pergunta
from certificado import certificado
from formulario import formulario
from formularioPergunta import formularioPergunta
from documento import documento

def main():
    #inserirEmpresa()
    #inserirUsuario()
    inserirPerguntas()
    inserirFormularios()
    relacionarFormularioPergunta()
    inserirRespostas()
    inserirCertificados()
    inserirDocumentos()

def inserirEmpresa():
    qntdAtual = 0
    for _ in range(100000):
        empresa().inserirBanco()
        qntdAtual += 1
        if qntdAtual % 100 == 0:
            print(f"{qntdAtual} empresas já cadastradas!")

def inserirUsuario():
    qntdAtual = 0
    for _ in range(100000):
        usuario().inserirBanco()
        qntdAtual += 1
        if qntdAtual % 100 == 0:
            print(f"{qntdAtual} usuários já cadastrados!")

def inserirRespostas():
    qntdAtual = 0
    for _ in range(100000):
        resposta().inserirBanco()
        qntdAtual += 1
        if qntdAtual % 100 == 0:
            print(f"{qntdAtual} respostas já cadastradas!")

def inserirPerguntas():
    qntdAtual = 0
    for _ in range(100000):
        pergunta().inserirBanco()
        qntdAtual += 1
        if qntdAtual % 100 == 0:
            print(f"{qntdAtual} perguntas já cadastradas!")

def inserirFormularios():
    qntdAtual = 0
    for _ in range(100000):
        formulario().inserirBanco()
        qntdAtual += 1
        if qntdAtual % 100 == 0:
            print(f"{qntdAtual} formulários já cadastrados!")

def relacionarFormularioPergunta():
    qntdAtual = 0
    for _ in range(100000):
        formularioPergunta().inserirBanco()
        qntdAtual += 1
        if qntdAtual % 100 == 0:
            print(f"{qntdAtual} relacionamentos entre formulários e perguntas já cadastrados!")

def inserirCertificados():
    qntdAtual = 0
    for _ in range(100000):
        certificado().inserirBanco()
        qntdAtual += 1
        if qntdAtual % 100 == 0:
            print(f"{qntdAtual} certificados já cadastrados!")

def inserirDocumentos():
    qntdAtual = 0
    for _ in range(100000):
        documento().inserirBanco()
        qntdAtual += 1
        if qntdAtual % 100 == 0:
            print(f"{qntdAtual} documentos já cadastrados!")

if __name__ == "__main__":
    main()
