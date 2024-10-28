'''
Nombre:
Fecha:
Descripción:
Ejemplos de uso de los operadores relacionales.
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
numero1 = float(input("Ingresa un número decimal: "))
numero2 = float(input("Ingresa otro número decimal: "))

print()
print(f"¿Los números son iguales? {numero1 == numero2}")
print(f"¿Los números son diferentes? {numero1 != numero2}")
print(f"¿El número {numero1:.2f} es mayor que {numero2:.2f}? {numero1 > numero2}")
print(f"¿El número {numero1:.2f} es menor que {numero2:.2f}? {numero1 < numero2}")
print(f"¿El número {numero1:.2f} es mayor o igual que {numero2:.2f}? {numero1 >= numero2}")
print(f"¿El número {numero1:.2f} es menor o igual que {numero2:.2f}? {numero1 <= numero2}")