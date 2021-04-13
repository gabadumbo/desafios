from collections import Counter
import csv

nuevo_archivo = open('pelis_2020.txt', 'w', encoding='utf-8')
archivo = open('netflix_titles.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(archivo, delimiter=',')
paises = {}
next(csv_reader)

for i in csv_reader:
    if (i[1] == 'Movie') and (i[7] == '2020'):
        nuevo_archivo.write(i[2]+'\n')
    if i[5] in paises.keys():
        paises[i[5]] += 1
    else:
        paises[i[5]] = 1


max = dict(Counter(paises).most_common(5))
print('Los 5 paises con mas titulos: ')
print(max)

archivo.close()
nuevo_archivo.close()
