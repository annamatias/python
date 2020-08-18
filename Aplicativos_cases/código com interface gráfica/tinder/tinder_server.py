from flask import Flask, jsonify, request

app = Flask(__name__)

database = dict()
database['PESSOA'] = []
database['interesses'] = {}

#essa daqui eu só criei pra poder debuggar,
#os testes nao exigem ela
@app.route('/show_all')#verbo GET, 
                       #toda vez q eu nao escrevo explicitamente
def all():
    return jsonify(database)

@app.route('/reseta', methods=['POST'])
def reseta():
    database['PESSOA'] = []
    database['interesses'] = {}
    return 'banco resetado'
    

@app.route('/pessoas', methods=['GET']) #coloquei o get mas nao
                                        #precisava
def pessoas():
    return jsonify(database['PESSOA'])

@app.route('/pessoas', methods=['POST'])
def cria_pessoas():
    dicionario_recebido = request.json
    lista_pessoas = database['PESSOA']
    lista_pessoas.append(dicionario_recebido)
    return jsonify(database['PESSOA'])

class NotFoundError(Exception):
    pass

def localiza_pessoa(id_pessoa):
    for dic_pessoa in database['PESSOA']:
        if dic_pessoa['id'] == id_pessoa:
            return dic_pessoa
    raise NotFoundError

@app.route('/pessoas/<int:id_pessoa>')
def get_pessoa(id_pessoa):
    return jsonify(localiza_pessoa(id_pessoa))

'http://localhost:5003/sinalizar_interesse/9/3/'
@app.route('/sinalizar_interesse/<int:interessado>/<int:interessante>/', methods=['PUT'])
def sinalizar_interesse(interessado,interessante):
    try:
        d_interessado = localiza_pessoa(interessado)
        d_interessante = localiza_pessoa(interessante)
    except NotFoundError:
        return 'pessoa nao encontrada',404
    #d_interessado {'nome':'aurelia','id':3,'sexo':'mulher','buscando':['mulher']}
    #d_interessante {'nome':'maximus','id':9,'sexo':'homem','buscando':['mulher']}
    if 'buscando' in d_interessado:
        lista_dos_generos_buscados = d_interessado['buscando'] #['mulher']
        if 'sexo' in d_interessante: #'homem'
            if d_interessante['sexo'] not in lista_dos_generos_buscados:
                return {'erro':'interesse incompativel'}, 400
    #ate aqui
    database['interesses'] #meu dicionario de interesses
    if interessado not in database['interesses']:
        database['interesses'][interessado] = []
    lista_do_interessado = database['interesses'][interessado]
    lista_do_interessado.append(interessante)
    return 'ok',200 #mas se eu nao digitasse 200, o cod status seria 200 automaticamente

@app.route('/sinalizar_interesse/<int:interessado>/<int:desinteressante>/', methods=['DELETE'])
def remover_interesse(interessado,desinteressante):
    try:
        localiza_pessoa(interessado)
        localiza_pessoa(desinteressante)
    except NotFoundError:
        return 'pessoa nao encontrada',404
    database['interesses'] #meu dicionario de interesses
    if interessado not in database['interesses']:
        database['interesses'][interessado] = []
    lista_do_interessado = database['interesses'][interessado]
    if desinteressante in lista_do_interessado:
        lista_do_interessado.remove(desinteressante)
    return 'ok',200 #mas se eu nao digitasse 200, o cod status seria 200 automaticamente



#crio usuario 5 e 9
#dicionario de interesses está vazio
#ele nao tem {5:[]}
#ele está assim {}
#vou consultar os matches do 5
# se eu fizer database['interesses'][pessoa], sem pensar
# a chave pessoa (no caso 5) nao esta no dicionario
# eu tomo um keyerror
#entao eu preciso tomar cuidado com isso

#quero a lista do usuário.
#mas quando é que a lista surje?
#quando o usuário passa a ser uma CHAVE do dicionario database['interesses']?
#só quando ele registra o primeiro interesse
def lista_de_interesses(id_pessoa):
    if id_pessoa in database['interesses']:
        return database['interesses'][id_pessoa]
    return []

#get('http://localhost:5003/matches/9')
@app.route('/matches/<int:usuario>')
def matches_do_usuario(usuario):
    try:
        localiza_pessoa(usuario)
    except NotFoundError:
        return 'pessoa nao encontrada',404
    matches = []
    lista_do_interessado = lista_de_interesses(usuario)
    for pessoa in lista_do_interessado:
        lista_da_pessoa = lista_de_interesses(pessoa)
        if usuario in lista_da_pessoa:
            matches.append(pessoa)
    return jsonify(matches)


if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
