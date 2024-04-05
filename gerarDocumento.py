import secrets;

def gerarDocumento():
    url_documento = secrets.token_urlsafe(32);
    return(url_documento)