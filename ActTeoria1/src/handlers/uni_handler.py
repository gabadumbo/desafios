import csv
import json


def make_data():
    ''' Hace el analisis de la data para la GUI y para el json '''
    csv_reader = csv.reader(
        open('src/csvs/uni.csv', 'r', encoding='utf-8'), delimiter=',')

    paises = 'Argentina Uruguay Chile Brazil Perú Paraguay Bolivia Colombia Venezuela'

    # Las top 30 universidades en ranking universitario en países de America año 2020
    data_json = {}
    cont = 0
    for row in csv_reader:
        if row[3] in paises:
            print(' - ', row[2], ' - ')
            cont += 1
            data_json[cont] = {'Universidad': row[2], 'País': row[3],
                               'Ranking mundial': row[1], 'Ranking nacional': row[4]}
        if cont == 30:
            break

    with open("exportados/analisis_uni.json", 'w', encoding='utf-8') as f:
        json.dump(data_json, f, indent=4, ensure_ascii=False)

    print('Exportado a JSON con éxito a la carpeta exportados!')
