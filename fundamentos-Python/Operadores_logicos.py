'''
Nombre:Rosalinda Aquino Pérez
Fecha:28/Octubre/2024
Descripción: Ejemplos de uso de los operadores relacionales.
'''

"""
Los operadores lógicos permiten combinar expresiones booleanas (verdadero o falso) para crear condiciones más complejas.
Estos operadores nos permiten realizar operaciones lógicas como "y", "o" y "no", lo que nos da la capacidad de tomar 
decisiones más sofisticadas dentro de nuestros programas.
"""

expresion1 = input("Ingresa un valor (Si/No): ")# Se solicita por consola al usuario que se ingrese dos valores (Si/No).
expresion2 = input("Ingresa otro valor (Si/No): ")# Se solicita por consola al usuario que se ingrese otro valor (Si/No).

# Las cadenas se convierten a expresiones booleanas (ver Fundamentos-Python -> Entrada_conversiones.py).
expresion1 = expresion1.lower() == "si"
expresion2 = expresion2.lower() == "si"

# Se imprimen mensajes sobre operaciones lógicas.
print(f"¿Ambas expresiones fueron 'si'? {expresion1 and expresion2}")
print(f"¿Alguna expresión fue 'si'? {expresion1 or expresion2}")
print(f"Lo contrario de la primera expresión es: {not expresion1}")
print(f"Lo contrario de la segundo expresión es: {not expresion2}")