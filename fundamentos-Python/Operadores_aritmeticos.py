'''
Nombre:Rosalinda Aquino Pérez
Fecha:28/Octubre/2024
Descripción: Ejemplos de uso de los operadores aritméticos.
'''
"""
Los operadores aritméticos en Python son los siguientes:
- Suma (+).
- Resta (-).
- Multiplicación (*).
- División (/).
- División entera (//).
- Módulo (%).
- Exponenciación (**).
"""
# Se solicitan dos números enteros al usuario.
numero1 = int(input("Ingresa un número entero: "))#Muestra un mensaje en pantalla pidiendo un número al usuario, esté de recibe como cadena y lo convierte a tipo entero.
numero2 = int(input("Ingresa otro número entero: "))#Muestra un mensaje en pantalla pidiendo un segundo número al usuario, esté de recibe como cadena y lo convierte a tipo entero.

# Se realizan las operaciones aritméticas.
print()
print("  ***   Ejemplos de uso de los operadores aritméticos   ***")

print(f"La suma de ({numero1} + {numero2}) es: {numero1 + numero2}")#Se realiza la suma de las dos variables número1 y número2 y se muestra en pantalla.
print(f"La resta de ({numero1} - {numero2}) es: {numero1 - numero2}")#Se realiza la resta de las dos variables número1 y número2 y se muestra en pantalla.
print(f"La multiplicación de ({numero1} * {numero2}) es: {numero1 * numero2}")#Se multiplicación la suma de las dos variables número1 y número2 y se muestra en pantalla.
print(f"La división de ({numero1} / {numero2}) es: {(numero1 / numero2):.2f}")    # Notar la forma para mostrar dos decimales.
print(f"La división entera de ({numero1} // {numero2}) es: {numero1 // numero2}")#Se realiza la division  de las dos variables número1 y número2 y se muestra en pantalla.
print(f"El módulo de ({numero1} % {numero2}) es: {numero1 % numero2}")#Se realiza el módulo de las dos variables número1 y número2 y se muestra en pantalla.
print(f"La exponenciación  de ({numero1} ** {numero2}) es: {numero1 ** numero2}")#Se eleva la variable numero1, dependiendo de la cantidad de la variable número2.