"""
Nombre: Rosalinda Aquino Pérez
Descripción del programa:
Este programa dibuja una escalera, en donde el usuario ingresa el número de escalores.
Si el número es positivo, la escalera será ascendente.
Si el número es negativo, la escalera será descendente.
"""

numero_escalones=None
espacio=" "
escalera=None
def escalera_ascendente(numero_escalones,espacio,escalera):
    while numero_escalones != 0:
        print("***  Ejercicio 1. La escalera.  ***")
        numero_escalones=int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:"))
        if numero_escalones>0:
            for i in range(numero_escalones):
                escalera= " " * i + "_|"
                print(f"{escalera}")
        elif numero_escalones < 0:
            for i in range(-1,numero_escalones):
                espacio = numero_escalones - i -1
                escalera=" " * espacio + "_|"
                print(f"{escalera}")
        elif numero_escalones == 0:
            print("Saliendo del programa.")
        else:
            print("Opción no válida.")
    return numero_escalones

numero_escalones=escalera_ascendente(numero_escalones,espacio,escalera)