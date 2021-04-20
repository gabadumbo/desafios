from collections import Counter
import csv
clasificaciones = {}

with open('appstore_games.csv', 'r', encoding='utf-8') as juegos:
    csv_reader = csv.reader(juegos, delimiter=',')
    next(csv_reader)

    print('Lista de juegos disponibles en español: ')
    for juego in csv_reader:
        if ('ES' in juego[12]) and (juego[7] == '0'):
            print(juego[2])
        if juego[6] != '':  # descarto los que no tienen clasificacion
            clasificaciones[juego[2]] = (int(juego[6]), juego[4])

max = dict(Counter(clasificaciones).most_common(10))
print('Los iconos de los 10 juegos con mejor clasificacion:')
for i in max:
    print(f'{max[i][1]}')
