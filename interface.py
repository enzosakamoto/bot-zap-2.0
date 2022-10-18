import PySimpleGUI as sg

# Layout
sg.theme('LightBlue4')
layout = [
    [sg.Push(), sg.Text('Bot para enviar mensagem para contatos no WhatsApp'), sg.Push()],
    [sg.Text('Digite o nome do contato: '), sg.Input(key = '-contato-', size = (40, 1)), sg.Button('Adicionar', key= '-botao_contato-')],
    [sg.Text('Digite a mensagem: '), sg.Input(key = '-mensagem-'), sg.Button('Adicionar', key= '-botao_mensagem-')],
    [sg.Text('Quantas mensagens deseja enviar [cada]: '), sg.Input(key = '-quantidade-', size = (27,1)), sg.Button('Adicionar', key= '-botao_qntmensagem-')],
    [sg.Push(), sg.Text('Selecione o seu tema do WhatsApp Web:'), sg.Push()],
    [sg.Push(), sg.Output(key = '-output-', size = (60,10)), sg.Push()],
    [sg.Push(), sg.Button('Limpar mensagens!'), sg.Button('Limpar contatos!'), sg.Button('Limpar tudo!'), sg.Push()],
    [sg.Push(), sg.Button('Enviar'), sg.Button('Sair'), sg.Push()],
    [sg.Push(), sg.Text('Versão 0.2')]
]