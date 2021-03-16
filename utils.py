import json

def extract_route(requisicao):
    c = 0
    g = ''
    rota = ''
    stop = False
    for k in requisicao:
        if not stop:
            if k == ' ':
                c = c + 1
            if c == 1:
                rota = rota + k
            if k == ' ' and c > 1:
                stop = True
              
    rota = rota[2:]

    return rota

def read_file(path):
    r=''
    t = str(path)
    s = t.split('.',1)[1] 
    if s == 'txt' or s == 'html' or s == 'css' or s == 'js':
        f = open(path, 'rt', encoding='utf-8')
        r = f.read().encode()
    else:
        f = open(path, 'rb')
        r = f.read()
    return r

# def load_data(file):
#     file_r = 'data/' + file
#     with open(file_r) as json_file:
#         data = json.load(json_file)
#     return data

def load_template(path):
    template = 'templates/' + path
    content = open(template).read()
    return content

# def addNote(note):   
#     with open('data/notes.json', 'r') as data_file:
#         data = json.load(data_file)
#     data.append(note)
#     with open('data/notes.json', 'w') as data_file:
#         data = json.dump(data, data_file)
            

def build_response(body='', code=200, reason='OK', headers=''):
    response = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n\n' + body 
    if headers != '':
        response = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n' + headers +'\n\n' + body
   
    response = bytes(response, 'utf-8')
    return response
