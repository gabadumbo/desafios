import PySimpleGUI as sg
from src.windows import menu
from src.handlers import uni_handler, lib_handler


def start():
    ''' Ejecuta la ventana '''
    window = loop()
    window.close()


def loop():
    '''Loop de la ventana'''
    window = menu.build()

    while True:
        event, values = window.read()
        if event == '-QUIT-':
            break
        elif event == '-UNI-':
            uni_handler.make_data()
            sg.popup('Exportado a /exportados!\n\nAnálisis: 30 mejores universidades de America del Sur (2015)\n',
                     title='Análisis realizado'
                     )
        elif event == '-LIB-':
            lib_handler.make_data()
            sg.popup('Exportado a /exportados!\n\nAnálisis: Los 50 países con mayor Libertad humana (2018)\n',
                     title='Análisis realizado'
                     )

        print(event, values)

    return window
