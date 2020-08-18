
'''
Um dicionário é muito semelhante a uma lista.

Tomemos a lista [10,20,30]. As posições dela são 0,1 e 2.
lista[0] vale 10, lista[1] vale 20 e lista[2] vale 30.

A diferença entre dicionários e listas é que um dicionário
pode ter as posições que a gente quiser.

Um dicionário pode ter as posições 3, 9 e 11
(sem ter as posições 0,1,2,4,5,6,7,8, nem 10)

Na verdade, como podemos ver no exemplo a seguir,
um dicionário pode ter as posições "marcos", "marcos-cel" e "maria".

(oficialmente, um dicionário não tem "posições",
mas sim chaves)

'''
agenda_exemplo = {}
agenda_exemplo['marcos']=32112232
agenda_exemplo['marcos-cel']=988887788
agenda_exemplo['maria']=44332212 

'''
Rode o codigo no IDLE apertando F5

Se você digitar agenda_exemplo['maria'],
deverá ver o telefone da maria
'''

'''
Crie uma função consulta que recebe uma agenda (um dicionário)
e uma pessoa, e retorna o telefone dessa pessoa
'''

#erro: em vez de usar a agenda que foi passada,
#ignorei ela e usei uma nova
def consulta(agenda, pessoa):
  agenda = {}
  return agenda[pessoa]

#erro: em vez de usar a agenda que foi passada,
#ignorei ela e usei uma nova
def consulta(agenda, pessoa):
  return agenda['pessoa']


#certo
def consulta(agenda, pessoa):
  return agenda[pessoa]



'''
Crie uma função adiciona que recebe uma agenda
(um dicionário)
uma pessoa e um telefone, e adiciona o
telefone dessa pessoa na agenda

Adicionar um item num dicionário é simples
dicionario['chave'] = valor
'''
agenda_exemplo = {}
agenda_exemplo['marcos']=32112232
agenda_exemplo['marcos-cel']=988887788
agenda_exemplo['maria']=44332212 

agenda_alunos = {}
agenda_alunos['gustavo']= 4444444444
agenda_alunos['millene']= 8888888888
agenda_alunos['luiz']= 8888888888


#funciona
def adiciona(agenda,pessoa,telefone):
  agenda[pessoa] = telefone
  return agenda

'''
Rode o codigo no IDLE apertando F5

Ai, você pode testar sua função adiciona manualmente e também 
fazer o runTests
'''

'''
Uma terceira feature que precisamos para a nossa agenda é
a possibilidade de verificar se uma pessoa já está na base de dados.

Simplesmente verificar agenda['pessoa'] não funciona:
se você acessar uma pessoa que não existe,
o python dará um KeyError.

Precisamos, então usar o seguinte: 'chave' in dicionario 
    isso é um teste que retorna True se a chave
    está no dicionário, e False caso contrário.

Temos, por exemplo, os prints seguintes,
que verificam se algumas pessoas estao na agenda
'''


#pessoa = 'marcos'
#print('a string da variavel pessoa é uma chave da agenda?')
#print(pessoa in agenda_exemplo)

'''
Crie uma função verifica, que recebe uma agenda
e um nome de pessoa, e verifica se a pessoa
está na agenda (retorna True se
a pessoa está e False caso contrário)
'''

#da um keyerror para as chaves que nao existem,
# nao funciona
def verifica(agenda,pessoa):
  if agenda[pessoa]:
    return True
  else:
    return False

#funciona
def verifica(agenda,pessoa):
  if pessoa in agenda:
    return True
  else:
    return False

def verifica(agenda,pessoa):
  return pessoa in agenda

  


''' 
Para definir um dicionário vazio, fazemos o seguinte:
'''
vazio = {}


'''
Usando seus conhecimentos de dicionário até agora, 
crie uma função conta_letras que recebe uma palavra e retorna
um dicionário com o número de ocorrências de cada letra.

por exemplo, conta_letras('abacaxi') deve
retornar o dicionário {'a':3,'b':1,'c':1,'x':1}

NAO USE nenhuma função mágica do python. Escreva a lógica
usando dicionários.

O seguinte trecho de codigo pode ser util:
>>> palavra='ganancia'
>>> nro_a = 0
>>> for letra in palavra:
	print('estou olhando para',letra)
	if letra == 'a':
		nro_a = nro_a+1

		
estou olhando para g
estou olhando para a
estou olhando para n
estou olhando para a
estou olhando para n
estou olhando para c
estou olhando para i
estou olhando para a
>>> nro_a
3
'''
#erro: letra in palavra
def conta_letras(palavra):
    conta={}
    for letra in palavra:
      #se a letra nao apareceu
      if letra not in palavra:
      #associa a chave letra ao valor 1
        conta[letra] = 1
      #se a letra ja apareceu
      else:
      #associa a chave letra a um valor maior do que ela ja tinha
        conta[letra] = conta[letra]+1
    return conta
#funciona
def conta_letras(palavra):
    conta={}
    for letra in palavra:
      #se a letra nao apareceu
      if letra not in conta:
      #associa a chave letra ao valor 1
        conta[letra] = 1
      #se a letra ja apareceu
      else:
      #associa a chave letra a um valor maior do que ela ja tinha
        conta[letra] = conta[letra]+1
    return conta


'''
Agora, vamos usar listas e dicionários para criar uma agenda 
um pouco mais completa. Veja o exemplo
'''

agenda_melhor1 = {
        'lucas (professor)': {
            'email': 'lucas.goncalves@faculdadeimpacta.com.br',
            'telefones': [11999888999, 1177788899]
            }, #meu email está correto, meus telefones nao :P
        'maria' : {
            'email':'maria.aparecida@exemplo.com',
            'telefones':[84999777444]
            },
        'lucas': {
            'telefones':[1177788899]     
            }
        }
def email(agenda,pessoa):
    return agenda[pessoa]['email']

def telefone_principal(agenda,pessoa):
    return agenda[pessoa]['telefones'][0]

def sem_email(agenda):
  resposta = []
  for pessoa in agenda:
    #1 a pessoa tem email?
    #2 o dicionario da pessoa tem email?
    #3 o valor que o dicionario agenda associa a pessoa tem a chave
    #email?
    if 'email' not in agenda[pessoa]:
        #coloco essa pessoa na lista dos sem email
        resposta.append(pessoa)
  return resposta

'''
Crie uma função conta telefones, que recebe uma agenda (nessa versão
mais nova) e retorna a quantidade de números de telefone registrados.

Se houver telefones repetidos (o exemplo agenda_melhor1 tem!), 
conte as repetições (então, para agenda_melhor1 a resposta deve
ser 4, por mais que o mesmo número apareça no item lucas
e no item lucas (professor)
'''

def conta_telefones(agenda):
    return 12

'''
Por ultimo, vamos criar uma funcao conta_ocorrencias
que dirá quantas vezes um telefone ocorre na agenda.

Ela recebe uma agenda melhorada (um dicionário nesse formato
que estamos usando) e devolve um dicionário. As chaves são
os números de telefone, e os valores, as vezes que cada 
número apareceu na agenda
'''

def conta_ocorrencias(agenda):
    return {1122224444:3}


import unittest

agenda_testes1 = {
        'joao':22222222,
        'jose':33333333,
        }

#agendas melhoradas
agenda1 = {}
alfabeto  = 'abcde'
for c in alfabeto:
    agenda1[c] = {'telefones':[1122233344]} #uma agenda cujas pessoas sao as primeiras 5 letras
agenda2 = {}
vogais  = 'aeiouy'
for c in vogais:
    agenda2[c] = {'telefones':[11321321321]} #uma agenda cujas pessoas sao todas as vogais
agenda2['fulano'] = {'email':'fulano@exemplo.com', 'telefones':[1144440000]}
agenda3 = {}
pessoas = ['marcia','ana','marcos','heitor'] 
for p in pessoas:
    agenda3[p] = {'telefones':[1123232323]}
agenda3['fulano'] = {'email':'fulano@exemplo.com','telefones':[11777888999,1122222222]}

class TestPartOne(unittest.TestCase):

    def test_05_email(self):
        self.assertEqual(email(agenda_melhor1,'lucas (professor)'),'lucas.goncalves@faculdadeimpacta.com.br')
        self.assertEqual(email(agenda_melhor1,'maria'),'maria.aparecida@exemplo.com')
        self.assertEqual(email(agenda2,'fulano'),'fulano@exemplo.com')
        self.assertEqual(email(agenda3,'fulano'),'fulano@exemplo.com')


    def test_06_telefone_principal(self):
        self.assertEqual(telefone_principal(agenda_melhor1,'lucas (professor)'),11999888999)
        self.assertEqual(telefone_principal(agenda_melhor1,'maria'),84999777444)
        self.assertEqual(telefone_principal(agenda_melhor1,'lucas'),1177788899)
        self.assertEqual(telefone_principal(agenda1,'a'),1122233344)
        self.assertEqual(telefone_principal(agenda2,'a'),11321321321)
        self.assertEqual(telefone_principal(agenda3,'ana'),1123232323)
        self.assertEqual(telefone_principal(agenda3,'fulano'),11777888999)

    def test_07_sem_email(self):
        self.assertEqual(set(sem_email(agenda1)),set(list(alfabeto)))
        self.assertEqual(set(sem_email(agenda2)),set(list(vogais)))
        self.assertEqual(set(sem_email(agenda3)),set(pessoas))

    def test_08_conta_telefones(self):
        self.assertEqual(conta_telefones(agenda1),5)
        self.assertEqual(conta_telefones(agenda2),7)
        self.assertEqual(conta_telefones(agenda3),6)
    
    def test_09_conta_ocorrencias(self):
        self.assertEqual(conta_ocorrencias(agenda1),{1122233344:5})
        self.assertEqual(conta_ocorrencias(agenda2),{11321321321:6, 1144440000:1})
        self.assertEqual(conta_ocorrencias(agenda3),{1123232323:4, 11777888999:1,1122222222:1})

    

        


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartOne)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

try:
  from dicionarios_gabarito import *
except:
  pass

runTests()
