'''
Nombre:Rosalinda Aquino Pérez.
Fecha:31/Octubre/2024
Descripción: Uso de la sentencia de control if.
'''

"""
La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
 dependiendo de si una condición se cumple o no.
Sintaxis:
if condición:
    # Código a ejecutar si la condición es verdadera. Notar que hay que dejar un espacio de tabulador.
# Código que se continúa ejecutando. Notar que ya no hay espacio y está a la misma altura que el if.
"""

print("  ***  Programa que determina si eres mayor de edad  ***")#Imprime un mensaje en consola.
numero = int(input("Ingresa tu edad: "))#Se muestra en pantalla un letrero donde solicita que ingrese su edad al usuario.
if numero >= 18:#Se declara una condicional, donde verifica si el contenido de la variable numero es mayor o igual a 18.
    print("Eres mayor de edad.")#Si está conccdicional resulta verdadera, se imprime en consola el mensaje, "eres mayor de edad".

print("Este código se ejecuta después de evaluarse la sentencia if.")#Muestra un mensaje en consola.

# Probar qué pasa con espacios simples, no dejando una línea entre ambas funciones print()
# y que ambos print() se encuentren a la misma altura.
#sia ambas se encuentarn a la misma altura el segundo print también formaria parte del condicional, if.