import sys, time, telepot, random
from telepot.loop import MessageLoop

menssagens = ['Olá', 'E aí?', 'HOLAAAA']
mensagem = random.choice(menssagens)

def recebido():
    commando = msg['text']
    opcoes(msg)

def opcoes(msg):
    chat_id = 1559056258

    print(str(random.choice(menssagens)))

    if commando == "/temp":
       bot.sendMessage('1559056258', random.randint(1,100))
    elif commando == "/frase":
       bot.sendMessage('1559056258', mensagem)

bot = telepot.Bot('1559056258:AAE1TxKeGkldCakhih47vvNbE1l3PDJHbcs')
bot.message_loop(recebido)
