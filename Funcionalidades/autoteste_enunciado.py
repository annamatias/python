#!bin/python
from flask import Flask,jsonify,abort
from flask import make_response
from flask import request


app = Flask(__name__)

questoes_iniciais = [
    {
        'id': 1,
        'pergunta': 'O que quer dizer RPC?',
        'erradas': ['Random Person Changer', 'Renato passa pelo centro' ],
        'corretas': ['Remote procedure call']
    },
    {
        'id': 2,
        'pergunta': 'Quanto vale 2**6?',
        'erradas': [12,36,26,32],
        'corretas': [64]
    }
]

respostas_iniciais = {
        'marcio':{1:'Random Person Changer'},
        'maria':{1:'Remote Procedure Call', 2: 64},
        }
import copy
def reseta():
    global respostas
    global questoes
    respostas = copy.deepcopy(respostas_iniciais)
    questoes = copy.deepcopy(questoes_iniciais)

reseta() #quando eu rodo isso eu crio as variaveis respostas e questoes
         #se sao as variaveis que você deve manipular

@app.route('/autoteste/reseta', methods = ['POST'])
def reseta_request():
    reseta()
    return {'status':'resetado'}

@app.route('/')
def index():
        return "Testes automáticos!"

'''
REPARE:

Você deve alterar os objetos respostas e questoes

NAO ALTERE NUNCA os objetos respostas_iniciais e questoes_iniciais
'''


'''
Ao acessar a URL /autoteste/questoes o usuario deve receber
uma lista completa de todas as questoes
'''
@app.route('/autoteste/questoes')
def todas_questoes():
    return jsonify(questoes)

'''
    Verifica se é possivel baixar o dicionario de respostas
    do servidor, acessando a url /autoteste/respostas com o verbo GET
'''

@app.route('/autoteste/respostas/')
def _respostas():
    return jsonify(respostas)

'''
Podemos acessar uma questao especifica na URL
/autoteste/questao/<int:q_id>

Se a questao existir, retorne a questao

Se nao existir, retorne um texto de erro e o codigo 404
'''
@app.route('/autoteste/questao/<int:q_id>') 
def busca_questoes(q_id):
    try:
        if q_id == 1:
            return jsonify(questoes_iniciais[0])
        elif q_id == 2:
            return jsonify(questoes_iniciais[1]) #entendi, retornar o dicionario todo no caso? (retornar o dicionario todo)
            #ok, yess precisp arrumar isso 'for dicionario in questoes'---> dica prof
        for q_id in questoes:
            return jsonify(questoes_iniciais)
    except:
        return 'Não foi encontrado',404
'''
Ao usarmos o verbo POST na url autoteste/questao

queremos criar uma nova questao.

no corpo da mensagem, enviamos o texto da questao (na chave pergunta),
uma lista de alternativas incorretas (na chave erradas) e uma lista
de alternativas corretas (na chave corretas).

Por exemplo:
    {
        'pergunta': 'O que quer dizer RPC?',
        'erradas': ['Random Person Changer', 'Renato passa pelo centro' ],
        'corretas': ['Remote procedure call']
    }

voce deve armazenar essa nova questao e retornar 
uma representacao JSON dela, com o codigo 201 (created)

Se um dos 3 campos estiver faltando, voce deve retornar um 
texto de erro, e o codigo 400
'''
@app.route('/autoteste/questao', methods=['POST'])
def cria_questao():
    questao_recebida = request.json
    todas_questoes = questoes
    ids = []
    for i in questoes:
        ids.append(i['id'])
    cont = 1
    questao_recebida['id'] = cont
    while questao_recebida['id']in ids:
        cont += 1
        questao_recebida['id'] = cont
    keys = ['pergunta', 'erradas', 'corretas']
    dici_keys = []
    for j in questao_recebida:
        dici_keys.append(j)
    for k in keys:
        if k not in dici_keys:
            return 'chave não encontrada,', 400
    todas_questoes.append(questao_recebida)
    return jsonify(questoes), 201

#Fazemos o mesmo teste anterior, mas queremos conferir o id da questão
@app.route('/autoteste/questao/<int_t_id>', methods=['POST'])
def confere_questao(t_id):
    questao_recebida = request.json
    todas_questoes = questoes
    ids = []
    for i in questoes:
        ids.append(i['id'])
    cont = 1
    questao_recebida['id'] = cont
    while questao_recebida['id']in ids:
        cont += 1
        questao_recebida['id'] = cont
    keys = ['pergunta', 'erradas', 'corretas']
    dici_keys = []
    for j in questao_recebida:
        dici_keys.append(j)
    for k in keys:
        if k not in dici_keys:
            return 'chave não encontrada,', 400
    todas_questoes.append(questao_recebida)
    return jsonify(questoes), 201
    #verifica id
    for idd in todas_questoes:
        if idd['t_id'] == todas_questoes['id']:
            return "ID ta na questao", 200
    return "ID não encontrado", 404

'''
Agora melhore sua funçao, fazendo com que, ao ser acrescentada uma
questão, ela automaticamente ganhe a próxima id disponível

(isso não necessariamente vai ser usado no proximo teste, mas vai
ser importante eventualmente)
'''

'''
Ao usarmos o verbo PUT na url 
/autoteste/questao/<int:q_id>/erradas

queremos adicionar mais alternativas erradas à questão.

enviamos, no corpo do request, uma lista de alternativas 
incorretas, e elas devem ser acrescentadas à questão.

por exemplo:
    {"erradas":[1,2,3,4,5]}

Se a questao não existir, devemos retornar o codigo 404
e uma mensagem de erro

Se a questão existir, devemos retornar a questao modificada
'''

'''
faça o mesmo, adicionando alternativas corretas extras
'''

'''
Agora melhore suas funções de adição de alternativas,
fazendo com que nao sejam adicionadas alternativas repetidas
'''


'''
Respondendo às perguntas

Fazendo um PUT na URL /autoteste/responder/1
o usuario 'fulano' pode responder à pergunta de id 1

ele deve mandar um json como o seguinte:
    { "usuario": "fulano",
      "resposta": "Remote Procedure Call"}
(o número da pergunta nao aparece no dicionario porque
já está na URL)

A sua resposta deve ser armazenada no dicionario respostas

Relembrando:
respostas_iniciais = {
        'marcio':{1:'Random Person Changer'},
        'maria':{1:'Remote Procedure Call', 2: 64},
        }
é um dicionario, cada pessoa é uma chave
o valor da pessoa é um dicionário
(o valor do maria é {1:'Remote Procedure Call', 2: 64})
olhando para esse dicionario, associado a maria, temos 2
chaves, uma para cada pergunta que ela respondeu.
O valor associado a chave 1 é a resposta que maria deu
para a pergunta 1

Se o usuário ja respondeu a pergunta, devemos retornar um erro 
descritivo e o codigo 409 (confito de edição)

Se ele respondeu com uma alternativa que nao está
nem na lista de corretas nem na lista de incorretas
, devemos retornar
um erro descritivo e o codigo 400 (bad request)

Se o usuário nao está na lista de respostas, devemos adicionar
ele (podemos criar um usuário novo ao enviar uma resposta!)
'''


'''
O usuario deve poder ver quantas perguntas ainda nao
respondeu, quantas acertou e quantas errou.

Acessando a url /autoteste/<username>/resultados com o verbo GET
O usuario deve receber um json como o seguinte:

    {
    "usuario": "fulano",
    "acertos": 3,
    "erros": 2,
    "nao respondidas": 2
    }

Por exemplo, se acessarmos a url /autoteste/maria/resultados,
devemos receber

    {
    "usuario": "maria",
    "acertos": 2,
    "erros": 0,
    "nao respondidas": 0
    }


ja vimos urls como /aluno/<int:id_aluno>
Agora, estamos recebendo uma string em vez de uma id.
Para isso, é só escrever /autoteste/<nome_aluno>/resultados no app.route
'''
       

if __name__ == '__main__':
   app.url_map.strict_slashes = False
   app.run(debug=True, host='0.0.0.0',port = 5004)
