import csv
import json
from collections import Counter
from operator import itemgetter


def make_data():
    ''' Hace el analisis y guarda la data en json '''
    csv_reader = csv.reader(
        open('src/csvs/lib.csv', 'r', encoding='utf-8'), delimiter=',')

    # Los 50 países que lideran el ranking en libertades humanas (civiles, religiosas, sexuales, economicas, de la mujer, etc) en 2018
    data_json = {}
    cont = 0

    filtro = list(
        filter(lambda x: x[1] == '2018' and float(x[6]) in range(1, 50), csv_reader))
    data = sorted(filtro, key=lambda x: float(x[6]))

    for i, x in enumerate(data):
        print(i, x[3])
        data_json[i+1] = {'País': x[3],
                          'Puntaje': x[5], 'Región': x[4], 'Código ISO': x[2]}

    with open("exportados/analisis_lib.json", 'w', encoding='utf-8') as f:
        json.dump(data_json, f, indent=4, ensure_ascii=False)

    print('Exportado a JSON con éxito a la carpeta exportados!')
