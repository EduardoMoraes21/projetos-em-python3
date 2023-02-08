# Projeto 2.0 - Decida por mim
# Faça uma pergunta para o pragrama e ele tera que dar uma respota

import random
import PySimpleGUI as sg

class DecidaPormim:
    def __init__(self):
        self.resposta = [
            'Com certaza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso não!',
            'Acho que ta na hora certa!'
        ]

    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text('Faça uma pergunta')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')],
        ]
        #Criar a janela
        self.janela = sg.Window('Decida por Mim!', layout=layout)
        while True:
            #Ler os valores
            self.eventos, self.valores = self.janela.Read()
            #Fazer algo com os valores

            if self.eventos == 'Decida por mim':
                print(random.choice(self.eventos))

decida = DecidaPormim()
decida.Iniciar()                