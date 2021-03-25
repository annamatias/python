import telepot
from Chatbot import Chatbot

bot = telepot.Bot('1559056258:AAE1TxKeGkldCakhih47vvNbE1l3PDJHbcs')
bot = Chatbot("Anna Karoliny")

def recebido(mensagem):
    print(mensagem['text'])

bot.message_loop(recebido) #método que fica roando em loop procurando novas mensagens.

while True:
    pass






"""
import telepot, time, random, sys
from telepot.loop import MessageLoop
  
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Comando recebido:',command)
 
    if command == '/COMANDO':
        #lines = open('arquivo.txt').read().splitlines()
        #mensagem = random.choice(lines)
        mensagem = 'eaiii'
        bot.sendMessage(chat_id, mensagem)
    elif command == '/COMANDO@SEU BOT':
        #lines = open('arquivo.txt').read().splitlines()
        #mensagem = random.choice(lines)
        mensagem = 'oiiiiiiiieeeeee'
        bot.sendMessage(chat_id, mensagem)
  
bot = telepot.Bot('1559056258:AAE1TxKeGkldCakhih47vvNbE1l3PDJHbcs')
bot.message_loop(handle)
print ('Esperando Mensagem...')
while 1:
    time.sleep(10)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg) # Use telepot.glance()para extrair “informações do título”. 
    print(content_type, chat_type, chat_id) #isso aqui vai me retornar o que foi enviado

    if content_type == 'text':
        chat_id = '1238273860:AAEDrtwMinclGjnxG-E80lxI2iEl0mt3qgw'
        bot.sendMessage(chat_id, msg['Olá']

#mensagens = ['Olá', 'E aí?', 'HOLAAAA']
token = sys.argv[1]  # get token from command-line

bot = telepot.Bot(token)
MessageLoop(bot, handle).run_as_thread() #praticamente ele notifica que foi enviado uma new msg
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
"""
    