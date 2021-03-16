from utils import *
from data import database
import urllib

def index(request):
    request = urllib.parse.unquote_plus(request)
    db = database.Database('banco')
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            
            k = chave_valor.split('=')
            params[k[0]] = k[1]
        db.add(database.Note(title = params['titulo'], content = params['detalhes']))
        return build_response(code=303, reason='See Other', headers='Location: /')
        

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)
    

    return build_response() + load_template('index.html').format(notes=notes).encode()
    #return build_response() + bytes(read_file('templates/index.html'), 'utf-8')