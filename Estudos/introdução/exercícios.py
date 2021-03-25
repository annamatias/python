
#=============================================
# Exercício faixa etária. 
'''
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")

Quando o usuário digitar 12, nenhuma condição será satisfeita! Repare que:

12 não é maior que 18 (idade > 18).
12 não é menor que 12 (idade < 12).
12 não é maior que 12 (idade > 12).
É preciso testar a igualdade através do ==.

Saiba também, que além do == (igualdade), > (maior) e < (menor), também temos >= (maior ou igual), <= (menor ou igual) e != (diferente).

todas as operadores de comparação:

< - menor que
> - maior que
<= - menor ou igual a
>= - maior ou igual a
== - igual a
!= - diferente de


#==============================================

usuario = input("Informe o usuário do sistema! \n")
pessoas = ['Flávio', 'Douglas', 'Nico']

if usuario in pessoas:
    print("Seja bem-vindo", usuario)

#===================================================
#Jogo de advinhar número

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou " , chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Parabéns! Você acertou!")
else:
    if(maior):
        print("O seu chute foi maior do que o número secreto!")
    elif(menor):
        print("O seu chute foi menor do que o número secreto!")

while rodadas >= tentativas:
    print("Teste de tentativas {} de {}".format(tentativas, rodadas))
    tentativas +=1

print("Fim do jogo")

#======================================================

#duas formas de fazer a formatação de string
dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017

print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim))

dia_inicio = 6
dia_final = 17
mes_ano = "janeiro"
Ano = 2021

print(f"Minhas ferias começou dia {dia_inicio} de {mes_ano} do ano de {Ano}, e termina dia {dia_final} de {mes_ano}")

#==============================================
#sobre Break e Continue.

for i in range(1,8):
    if(i == 5):
        continue #ele retorna o bloco de operação e não prossegue em frente, ou seja, no que tenha abaixo do código.
    print(i)

#break - esse comando tem a capacidade de parar o loop

#==============================================
#Formatação de strings

Segue o link da documentação que mencionei no video, nele tem vários exemplos de formatação:

https://docs.python.org/3/library/string.html#formatexamples

Nesse vídeo veremos um pouco mais sobre interpolação de strings. Para isso, vamos utilizar o console do Python 3.

No capítulo anterior, fizemos uma interpolação semelhante a essa:

>>> print("Tentativa {} de {}".format(1, 3))
Essa interpolação é útil para formatação de strings, quando temos um texto muito grande e precisamos inserir valores no meio dele, ao invés de ficarmos concatenando, trabalhando com várias strings separadas.

Mas a função format tem outras utilidades, então veremos mais alguns detalhes sobre essa função. O primeiro detalhe que veremos é que os parâmetros podem ser invertidos na string. Podemos dizer que queremos nas primeiras chaves o segundo parâmetro da função, e o primeiro parâmetro nas segundas chaves.

Fazemos isso passando o índice do parâmetro dentro das chaves. O primeiro parâmetro tem índice 0, o segundo 1, e daí por diante. Logo, basta passar o índice 1 nas primeiras chaves e o 0 nas segundas chaves:

>>> print("Tentativa {1} de {0}".format(1, 3))
Tentativa 3 de 1
Formatação de floats
Agora vamos trocar o exemplo, e formatar um valor em reais, por exemplo:

>>> print("R$ {}".format(1.59))
R$ 1.59
Só que um valor pode ter vários tamanhos e até duas casas decimais, por exemplo:

1.59
45.9
1234.97
O ideal é que esses valores sempre tenham a mesma formatação:

   1.59
  45.9
1234.97
Então precisamos preencher as lacunas, os espaços em branco. E a função format faz isso para nós. Primeiro precisamos dizer para ela que estamos recebendo um valor do tipo float, passando :f dentro das chaves da string:

>>> print("R$ {:f}".format(1.59))
R$ 1.590000
Podemos reparar que só de dizer que estamos passando um float, a formatação já muda, mas podemos manipulá-la, modificá-la, dizendo quantos números devem vir antes e depois do ponto. Queremos que após o ponto tenha apenas 2 números, logo:

>>> print("R$ {:.2f}".format(1.59))
R$ 1.59
Podemos testar passando um número de apenas uma casa decimal:

>>> print("R$ {:.2f}".format(1.5))
R$ 1.50
Ótimo, agora vamos testar com um número maior:

>>> print("R$ {:.2f}".format(1.5))
R$ 1.50
>>> print("R$ {:.2f}".format(1234.50))
R$ 1234.50
Mas queremos que o ponto fique sempre no mesmo local, ou seja, ele deve ser o quinto caractere. Para essa formatação, precisamos dizer quantos caracteres o número terá no máximo, no nosso caso são 7 (4 números, mais o ponto, mais as duas casas decimais). Então vamos passar o valor 7 dentro das chaves também:

>>> print("R$ {:7.2f}".format(1234.50))
R$ 1234.50
>>> print("R$ {:7.2f}".format(1.5))
R$    1.50
Ou seja, dos 7 caracteres, os três últimos serão o ponto mais dois números das casas decimais.

Agora espaços ficam na frente quando um número for menor! Deixando o ponto sempre como quinto caractere. Se quisermos preencher os espaços em branco com zeros, é só passar um 0 antes do 7:

>>> print("R$ {:07.2f}".format(1.5))
R$ 0001.50
Formatação de inteiros
Conseguimos formatar números inteiros também, não só números flutuantes. Para números inteiros, passamos a letra d:

>>> print("R$ {:07d}".format(4))
R$ 0000004
Podemos usar isso para formatar uma data:

>>> print("Data {:02d}/{:02d}".format(9, 4))
Data 09/04
>>> print("Data {:02d}/{:02d}".format(19, 11))
Data 19/11
Não se preocupe em decorar a sintaxe, o importante é saber que no Python existe a funcionalidade de interpolação de strings, e quando vocês realmente precisarem usar isso, olhem na documentação.

#====================================
#gerando numeros aleatorios com random

import random

#podemos utilizar random.random() que tera valores entre 0.0 até 1.0

random.random()

#ou podemos utilizar diretamente um numero inteiro com range

random.randrange(1,100) #sendo possiel determinar os parametros e intevalo de numeros.

#jogo

import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        if(maior):
            print("O seu chute foi maior que o número secreto")
            if (rodada == total_tentativas):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            if (rodada == total_tentativas):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))

print("Fim do jogo")
'''


