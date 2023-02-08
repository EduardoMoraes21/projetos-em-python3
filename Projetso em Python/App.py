import PySimpleGUI as sg

# Criar o layout
def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('Todo List',layout=layout,finalize=True)
# Criar a janela
janela = criar_janela_inicial()
# Criar as regras dessa janela
while True:
   event, value = janela.read()
   if event == sg.WIN_CLOSED:
        break 
   elif event == 'Nova Tarefa':
       janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
   elif event == 'Resetar':
       janela.closed()
       janela = criar_janela_inicial()