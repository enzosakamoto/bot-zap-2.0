from interface import *
from funcoes import *

# Interface
janela = sg.Window('Bot do zap', layout)

# Lista de variáveis
contatos = []
mensagens = []
qntMensagem = 0 # Para cada mensagem da lista 'mensagens'

# Leitura de eventos da interface
while True:
    eventos, valores = janela.read()

    # Condições de fechamento do programa
    if eventos in (sg.WIN_CLOSED, 'Sair'):
        break

    # Condição para adicionar contato na lista de contatos
    if eventos == '-botao_contato-':
        contatos.append(valores['-contato-'])
        janela['-contato-'].update('')
        janela['-output-'].update('')
        exibeOutput(contatos = contatos, mensagens = mensagens, quantidade = qntMensagem)

    # Condição para adicionar mensagem na lista de mensagens
    if eventos == '-botao_mensagem-':
        mensagens.append(valores['-mensagem-'])
        janela['-mensagem-'].update('')
        janela['-output-'].update('')
        exibeOutput(contatos = contatos, mensagens = mensagens, quantidade = qntMensagem)

    # Condição para adicionar a quantidade de mensagens a serem enviadas
    if eventos == '-botao_qntmensagem-':
        qntMensagem = int(valores['-quantidade-'])
        janela['-quantidade-'].update('')
        janela['-output-'].update('')
        exibeOutput(contatos = contatos, mensagens = mensagens, quantidade = qntMensagem)

janela.close()
