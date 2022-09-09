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
        if valores['-contato-'] != '':
            contatos.append(valores['-contato-'])
            janela['-contato-'].update('')
            janela['-output-'].update('')
            exibeOutput(contatos = contatos, mensagens = mensagens, quantidade = qntMensagem)
        else:
            sg.popup('Aviso!', 'Escreva um contato válido!')

    # Condição para adicionar mensagem na lista de mensagens
    if eventos == '-botao_mensagem-':
        if valores['-mensagem-'] != '':
            mensagens.append(valores['-mensagem-'])
            janela['-mensagem-'].update('')
            janela['-output-'].update('')
            exibeOutput(contatos = contatos, mensagens = mensagens, quantidade = qntMensagem)
        else:
            sg.popup('Aviso!', 'Escreva uma mensagem válida!')

    # Condição para adicionar a quantidade de mensagens a serem enviadas
    if eventos == '-botao_qntmensagem-':
        if valores['-quantidade-'].isdigit(): # Verifica se a quantidade digitada é um número
            qntMensagem = int(valores['-quantidade-'])
            janela['-quantidade-'].update('')
            janela['-output-'].update('')
            exibeOutput(contatos = contatos, mensagens = mensagens, quantidade = qntMensagem)
        else:
            sg.popup('Aviso!', 'Digite um valor inteiro!')

    # Condição para limpar todos os dados
    if eventos == 'Limpar tudo!':
        janela['-mensagem-'].update('')
        janela['-contato-'].update('')
        janela['-quantidade-'].update('')
        janela['-output-'].update('')
        mensagens, contatos, qntMensagem = [], [], 0
        exibeOutput(contatos = contatos, mensagens = mensagens, quantidade = qntMensagem)

    # Condição para enviar todos os dados armazenados
    if eventos == 'Enviar':
        if len(contatos) != 0 and len(mensagens) != 0 and qntMensagem != 0: # Verifica se os campos foram preenchidos
            if valores['-light-'] == True and valores['-dark-'] == False: # Verifica se o tema é Light
                for contato in contatos:
                    procuraContatoLight(contato = contato)
                    for mensagem in mensagens:
                        for i in range(qntMensagem):
                            escreveMensagem(mensagem = mensagem)
                        sleep(2)
            elif valores['-dark-'] == True and valores['-light-'] == False: # Verifica se o tema é Dark
                for contato in contatos:
                    procuraContatoDark(contato = contato)
                    for mensagem in mensagens:
                        for i in range(qntMensagem):
                            escreveMensagem(mensagem = mensagem)
                        sleep(2)
            else: # Retorna as demais condições
                sg.popup('Aviso!', "Marque as checkbox's corretamente!")
        else:
            sg.popup('Aviso!', 'Campos obrigatórios faltando!')

janela.close()
