#Gerador de Senhas utilizando PySimpleGUI
#Sera ultilazdo para gerar senha de e-mails

import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        #layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10,1)),sg.Input(key='size',size=(20,1))],
            [sg.Text('E-mail/Usuario',size=(10,1)),sg.Input(key='usuario',size=(20,1))],
            [sg.Text('Quantidades de carateres'), sg.Combo(values=list(range(30)),key='total_chras', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')],

        ]
        #declara janela
        self.janela = sg.Window('Password Generator',layout)
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@%$*'
        chars = random.choices(char_list, k=int(valores['total_chras']))
        new_pass = ''.join(chars)
        return new_pass
    
    def salvar_senha(self, nova_senha, valores):
        with open('senhas.text','a',newline='') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuario: {valores['usuario'], nova_senha: {nova_senha}}")
        
        print('Arquivo salvo')

gen =  PassGen()
gen.Iniciar()   
