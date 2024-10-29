'''
Nombre:Rosalinda Aquino Pérez
Fecha:28/Octubre /2024
Descripción:Uso de la sentencia de control if-else.
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
print("  ***  Programa que determina si un número es par o impar  ***")#Imprime un mensaje en la consola.
numero = int(input("Ingresa un número: "))  #Muestra un mensaje en consola pidiendo al usuario que ingrese un número, esté se recibé como cadena  y lo convierte a entero.
print()
if numero % 2 == 0: #Se declara una condicional, dondé verifica si el contenido de la variable numero es divisible entre 2 el residuo es cero.
    print("El número es par.")#Si la condición es verdadera, se imprime un mensaje "El número es par".

else:
    print("El número es impar.")#Si la condición no es verdadera, se imprime el siguiente mensaje: "El número es impar"