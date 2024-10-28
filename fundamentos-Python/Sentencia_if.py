'''
Nombre:
Fecha:
Descripción:
Uso de la sentencia de control if.
'''

"""
La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
 dependiendo de si una condición se cumple o no.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera. Notar que hay que dejar un espacio de tabulador.

# Código que se continúa ejecutando. Notar que ya no hay espacio y está a la misma altura que el if.
"""

# Ejemplo en donde se imprime un mensaje si el usuario tiene la mayoría de edad.
print("  ***  Programa que determina si eres mayor de edad  ***")
numero = int(input("Ingresa tu edad: "))#Se muestra en pantalla un letrero donde solicita que ingrese su edad al usuario.
if numero >= 18:#Se declara una condición, donde la varia
    print("Eres mayor de edad.")

print("Este código se ejecuta después de evaluarse la sentencia if.")

# Probar qué pasa con espacios simples, no dejando una línea entre ambas funciones print()
# y que ambos print() se encuentren a la misma altura.