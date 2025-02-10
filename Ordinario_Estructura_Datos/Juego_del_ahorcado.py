#Rosalinda Aquino Pérez
#juego del gato
import random

palabras=["manzana","colibri","gato","informatica"]#Creamos una lista de palabras
palabra_secreta=random.choice(palabras)#Elige una palabra aleatoria, de la lista que creamos.
cadena="-"*len(palabra_secreta)
intentos=0

while intentos<5:#Ciclo que se repite hasta que se acaben los intentos.
    letra=input("Ingrese una letra: ")#Solicita al usuario que ingrese una letra.
    cadena_nueva = ""
    if letra in palabra_secreta:#Comparar si la letra esta dentro de la palabra secreta.
        for i in range(len(palabra_secreta)):#Recorre la cantidad de letras que tiene la palabra.
            if palabra_secreta[i] == letra:
                cadena_nueva+=letra
            else:
                cadena_nueva+=cadena[i]
        cadena=cadena_nueva#actualiza la cadena
    else:
        intentos+=1
        print(f"Letra incorrecta.realizaste tu {intentos} intento.")
    print(cadena)
    if "-" not in cadena:
        print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
        break
else:
    print(f"Se ha terminado el jueguto, la palabra era:{palabra_secreta}")
