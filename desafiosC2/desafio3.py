total,cant = 0,0
nota = int(input("Ingresá una nota (-1 para finalizar): "))
lista_de_notas = []

while(nota != -1):
    cant += 1
    total += nota
    lista_de_notas.append(nota)
    nota = int(input("Ingresá una nota (-1 para finalizar): "))

promedio = total / cant
cant = 0
for nota in lista_de_notas:
    if(nota < promedio):
        cant+=1
        
print(f"""
El promedio es de {promedio}.
Y la cantidad de alumnos con nota menor al promedio es de {cant}
""")
