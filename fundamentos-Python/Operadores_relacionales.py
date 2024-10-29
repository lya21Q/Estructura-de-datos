'''
Nombre:Rosalinda Aquino Pérez
Fecha:28/Octubre/2024
Descripción: Ejemplos de uso de los operadores relacionales.
'''

"""
Los operadores relacionales son símbolos que se utilizan en programación para comparar dos valores. 
Estos operadores devuelven un valor booleano (verdadero o falso) dependiendo del resultado de la comparación. 
Son fundamentales para tomar decisiones dentro de un programa, ya que permiten construir expresiones condicionales 
que determinan el flujo de ejecución.

Operadores Relacionales Comunes:
Operador	Significado
==	Igual a
!=	Diferente de
>	Mayor que
<	Menor que
>=	Mayor o igual que
<=	Menor o igual que
"""

# Se solicitan dos números para realizar distintas operaciones relacionales.
numero1 = float(input("Ingresa un número decimal: "))# Se muestra un mensaje en pantalla solicitando al usuario un número decimal, el cual es recibido como cadena y lo convierte a decimal.
numero2 = float(input("Ingresa otro número decimal: "))# Se muestra un mensaje en pantalla solicitando al usuario un segundo número decimal, el cual es recibido como cadena y lo convierte a decimal.

print()
print(f"¿Los números son iguales? {numero1 == numero2}")#Se realiza una comparación si numero1 es igual a numero2 y se muestra el resultado.
print(f"¿Los números son diferentes? {numero1 != numero2}")#Se realiza una comparación si numero1 es diferente a numero2 y se muestra el resultado.
print(f"¿El número {numero1:.2f} es mayor que {numero2:.2f}? {numero1 > numero2}")#Se realiza una comparación si numero1 es mayor a numero2 y se muestra el resultado con solo dos decimales.
print(f"¿El número {numero1:.2f} es menor que {numero2:.2f}? {numero1 < numero2}")#Se realiza una comparación si numero1 es menor a numero2 y se muestra el resultado con solo dos decimales.
print(f"¿El número {numero1:.2f} es mayor o igual que {numero2:.2f}? {numero1 >= numero2}")#Se realiza una comparación si numero1 es mayor o igaul a numero2 y se muestra el resultado con solo dos decimales.
print(f"¿El número {numero1:.2f} es menor o igual que {numero2:.2f}? {numero1 <= numero2}")#Se realiza una comparación si numero1 es menor o igual a numero2 y se muestra el resultado con solo dos decimales.