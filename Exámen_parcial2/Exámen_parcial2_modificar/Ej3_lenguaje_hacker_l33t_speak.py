"""
Descripción del programa:
Este programa convierte un texto al lenguaje hacker (lenguaje leet o 1337). Esta escritura se caracteriza por reemplazar las letras por números y símbolos.

Lenguaje básico:
En el lenguaje básico se sustituye cada vocal por un número.
La A se convierte en un 4, la E en un 3, la I en un 1 y la O en un cero.
La letra U es una excepción, ya que no hay un número obvio, por lo que se sustituye por (_).

Lenguaje intermedio:
En el lenguaje intermedio también se sustituyen las consonantes por números o signos de puntuación.
Por ejemplo, la B se convierte en I3, la C en [, la D en ), la L en 1.
Revisa la "Leet speak alphabet" de la página anterior y toma la primera de las opciones para el lenguaje.
Nota que no hay caracteres acentuados, por lo no se deben de convertir.
"""

def menu():
    print("***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***")
    print("[1].- Convertir un texto a lenguaje básico.")
    print("[2].- Convertir un texto a lenguaje intermedio.")
    print("[0].- Salir.")
    op=int(input("Ingrese opción:"))
    return op

def convertir(op):

    if op == 1:
        texto=input("Ingrese texto a convertir: ")
    elif op == 2:
        texto=input("Ingrese texto a convertir: ")
        print("Texto convertido a lenguaje intermedio: ", texto)
    elif op == 0:
        print("Saliendo del programa.")
    else:
        print("Opciòn no valida.")