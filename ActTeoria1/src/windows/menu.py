import PySimpleGUI as sg
from src.handlers import icon_handler

sg.theme('DarkAmber')


def build():
    ''' Genera el layout y la ventana '''
    layout = [
        [sg.Text('¿Que datos analizamos?')],
        [sg.Button('Ranking universidades', key='-UNI-', size=(25, 2))],
        [sg.Button('Ranking libertades', key='-LIB-', size=(25, 2))],
        [sg.Button('Salir', key='-QUIT-', size=(25, 2), pad=(10, 20))]
    ]

    window = sg.Window(
        'Analisis de datos', layout, element_justification='c', size=(400, 280),
        element_padding=(10, 10), icon=icon_handler.getIcon('collectData.ico', 'dataIcon.jpg'),
        disable_close=True)

    return window
