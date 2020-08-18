from flask import Flask, jsonify, request
app = Flask(__name__) 

database = {}
database['ALUNO'] = []
database['PROFESSOR'] = []

@app.route('/reseta', methods=['POST'])
def reseta():
    database['ALUNO'] = []
    database['PROFESSOR'] = []
    return database

@app.route('/full_db')
def all():
  print('mostrando a db inteira')
  return jsonify(database) #converter de dict pra string

@app.route('/alunos')#se eu nao especifiquei, é GET
def alunos():
    return jsonify(database['ALUNO'])

def consulta_aluno_por_id(id_aluno):
    for dic_aluno in database['ALUNO']:
        if dic_aluno['id'] == id_aluno:
            return dic_aluno
    return False

@app.route('/alunos', methods=['POST'])#msm URL, verbo POST
def novo_aluno():
    novo_aluno = request.json #pego dicionario enviado
    if 'nome' not in novo_aluno:
        return {'erro': 'aluno sem nome'}, 400
    if consulta_aluno_por_id(novo_aluno['id']) != False:
        return {'erro':'id ja utilizada'}, 400
    database['ALUNO'].append(novo_aluno) #e coloco na lista
    return jsonify(database['ALUNO'])

#/alunos/100, /alunos/30 /alunos/5
@app.route('/alunos/<int:id_aluno>', methods=['GET'])#recebe um numero na url
def localiza_aluno(id_aluno):#passa o numero para a função
    
    for dic_aluno in database['ALUNO']:
        if dic_aluno['id'] == id_aluno:
            return jsonify(dic_aluno)
    return {'erro':'aluno nao encontrado'}, 404 #retorna o arquivo com o dic do erro
                                                # e o COD DE STATUS 404

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])#a url é a mesma acima, mas
                                                        #mudou o verbo
def deleta_aluno(id_aluno):
    for dic_aluno in database['ALUNO']:
        if dic_aluno['id'] == id_aluno:
            lista_de_dics_alunos = database['ALUNO']
            lista_de_dics_alunos.remove(dic_aluno)
            return jsonify({'status':'removido'})
    return {'erro':'aluno nao encontrado'}, 404 #retorna o arquivo com o dic do erro
                                                # e o COD DE STATUS 404

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def edita_aluno(id_aluno):
    for dic_aluno in database['ALUNO']:
        if dic_aluno['id'] == id_aluno:
            dic_aluno['nome'] = request.json['nome']
            #o novo nome no       o nome mandado
            # "banco"               no request
            return jsonify(dic_aluno)
    return {'erro':'aluno nao encontrado'}, 404 #retorna o arquivo com o dic do erro
                                                # e o COD DE STATUS 404


@app.route('/professores') #registrei uma URL
def professores(): #executo uma função
    return jsonify(database['PROFESSOR'])#e retorno uma string (que no caso
                                        #representa um dicionario)



@app.route("/") 
def hello(): 
    return "Bom dia pessoas!"

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True) 

    #pip install --upgrade Flask
    #pip install --user requests


"""
pip install flask --user
python 
import flask
"""
