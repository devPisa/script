import secrets;

class Documento():

    @classmethod
    def gerarDocumento(cls):
        url_documento = secrets.token_urlsafe(32);
        return(url_documento)