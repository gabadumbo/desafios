def encripto(s):
    """Recibe una cadena, y la devuelve con el cifrado César. """
    return ''.join(map(lambda x: chr(ord(x)+1), s))

