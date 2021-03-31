cant,total = 0,0
dicci = {}

nombre = input("Ingresa un nombre (<FIN> para finalizar): ")
while(nombre != "FIN"):
    nota = int(input(f"Ingresa la nota de {nombre}: "))
    dicci[nombre] = nota
    cant += 1
    total += nota
    nombre = input("Ingresa un nombre (<FIN> para finalizar): ")

promedio = total / cant
for nombre in dicci:
    if(dicci[nombre] < promedio):
        print(f"El alumno {nombre} tiene una nota por debajo del promedio.")
