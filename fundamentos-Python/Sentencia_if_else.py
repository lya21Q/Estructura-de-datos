'''
Nombre:
Fecha:
Descripción:
Uso de la sentencia de control if-else.
'''

"""
La sentencia if-else es una estructura de control fundamental que permite tomar decisiones en el código.
Dependiendo de si se cumple una determinada condición, el programa tomará un camino u otro.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera.

else:
    # Código a ejecutar si la condición es falsa.

# Código que se ejecuta sin importar la condición.
"""

# Ejemplo en donde se determina si un número es par o impar.
print("  ***  Programa que determina si un número es par o impar  ***")
numero = int(input("Ingresa un número: "))  # Solicitamos el número

# lógica para determinar si es par o impar
print()
if numero % 2 == 0:  # Implica que es par
    print("El número es par.")

else:
    print("El número es impar.")  # Implica que es impar