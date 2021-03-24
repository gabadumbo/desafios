palabra = input("Ingrese una palabra: ")

while(palabra != "FIN"):
    if(palabra[0] == palabra[-1]):
        print("Empieza y termina con la misma letra")
    palabra = input("Ingrese una palabra: ")
