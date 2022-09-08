import pyautogui
from time import sleep

# Box Mensagem 1486, 989
# Box Pesquisar 1149, 126
# Contato pesquisado 1126, 256

# Procura contato e clica nele
def procuraContato(contato):
    pyautogui.click(1149, 126, duration = 2)
    pyautogui.write(contato)
    pyautogui.click(1126, 256, duration = 2)
    sleep(2)

# Escreve a mensagem
def escreveMensagem(mensagem):
    pyautogui.write(mensagem)
    pyautogui.press('enter')

def exibeOutput(contatos, mensagens, quantidade):
    print('Contatos adicionados:')
    for e in contatos:
        print(e, end = ', ')
    print('\n\nMensagens adicionadas:')
    for e in mensagens:
        print(e, end = ', ')
    print('\n\nMensagens a serem enviadas [para cada mensagem adicionada]:')
    print(quantidade)

