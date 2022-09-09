import pyautogui
from time import sleep

# Resolução 1920 x 1080
# Box Mensagem 933, 979
# Box Pesquisar 367, 199
# Contato pesquisado 367, 330

# Procura contato e clica nele (tema Dark)
def procuraContatoDark(contato):
    pyautogui.click('assets/botao-pesquisar.png', duration = 2)
    pyautogui.write(contato)
    x_pesquisar, y_pesquisar = pyautogui.position()
    pyautogui.click(x_pesquisar, y_pesquisar + 129, duration = 2)
    sleep(2)

# Procura contato e clica nele (tema Light)
def procuraContatoLight(contato):
    pyautogui.click('assets/botao-pesquisar-light.png', duration = 2)
    pyautogui.write(contato)
    sleep(5)
    x_pesquisar, y_pesquisar = pyautogui.position()
    pyautogui.click(x_pesquisar, y_pesquisar + 129, duration = 2)
    sleep(2)

# Escreve a mensagem
def escreveMensagem(mensagem):
    pyautogui.write(mensagem)
    pyautogui.press('enter')

# Função para formatar o print no Output
def printFormatado(lista):
    i = 0
    while i < len(lista):
        print(lista[i], end = '')
        if i < len(lista) - 1:
            print(', ', end = '')
        i += 1

# Função para exibir as variáveis no campo de Output
def exibeOutput(contatos, mensagens, quantidade):
    print('Contatos adicionados:')
    printFormatado(lista = contatos)
    print('\n\nMensagens adicionadas:')
    printFormatado(lista = mensagens)
    print('\n\nMensagens a serem enviadas [para cada mensagem adicionada]:')
    print(quantidade)

