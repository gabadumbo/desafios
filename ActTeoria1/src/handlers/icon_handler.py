import platform


def getIcon(ico, img):
    '''Devuelve un icono .ico si esta en windows, sino una imagen (asi lo pide en la documentacion)'''
    os_name = platform.system()
    ruta = "src/icons/"

    if os_name == 'Windows':
        return ruta + ico
    elif os_name == 'Linux':
        return ruta + img
