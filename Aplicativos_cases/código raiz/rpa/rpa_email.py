#esses 2 import's servem para automatizar tarefas do pc, comandos de tela do pc, mouse e teclado.
import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

#abrir a nova aba
pyautogui.hotkey('crtl','t')
#entrar no link do sistema
link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'
pyperclip.copy(link)
pyautogui.hotkey("crtl","v")
pyautogui.press("enter")
print("executou")