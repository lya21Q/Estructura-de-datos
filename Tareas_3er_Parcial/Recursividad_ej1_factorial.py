"""
#Rosalinda Aquino
Instrucciones:

Escribe un programa de nombre Recursividad_ej1_factorial.py que realice lo que se indica en la descripción del programa.

Descripción del programa:
Este programa calcula el factorial de un número entero positivo ingresado por el usuario, utilizando recursividad.

Notar que: n! = n*(n-1)!
Para ello:
a) Solicite al usuario el número al que se requiere calcular el factorial, validando que tenga el formato adecuado.
b) Utilice una función recursiva para calcular el factorial, indicando el caso base y el caso recursivo.
c) Muestre el resultado en consola.
"""

def factorial(n: int) -> int:# Caso base: el factorial de 0 o 1 es 1.
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

def es_numero_valido(cadena: str) -> bool:# Verifica si la cadena es un número entero positivo.
    if cadena.isnumeric():
        return True
    else:
        return False

def main() -> None:
    print("*** Programa que calcula el factorial de un número entero positivo ***")
    print()

    num_cadena = input("Ingresa un número entero positivo: ")# Solicita al usuario un número y valida que sea un entero positivo.
    print()

    if es_numero_valido(num_cadena):# Si es un número válido, calcula y muestra el factorial.
        numero = int(num_cadena)
        resultado = factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
    else:# En caso contrario, finaliza el programa.
        print("Número no válido. Por favor, ingresa un número valido.")

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
