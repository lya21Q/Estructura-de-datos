"""
Escribe un programa de nombre Operadores_ejercicio2.py que realice lo siguiente:

Este programa determinará si una persona forma parte de la comunidad de la UNSIJ. Para ello:
"""

"""
a) Pregunte al usuario si es profesor de la UNSIJ (Si/No).
"""
variable=input("¿El profesor es de Unsij, (Si/No)?: ")
variable = variable.lower() == "si"
"""
b) Pregunte al usuario si es alumno de la UNSIJ (Si/No).
"""
variable1=input("¿El alumno es de Unsij, (Si/No)?: ")
variable1 = variable1.lower() == "si"
"""
c) La persona forma parte de la UNSIJ si es profesor o alumno de la UNSIJ.
"""
if variable == " Si" or variable == "Si":
    print("La persona forma parte de la Unsij ")
"""
d) Muestre el resultado en consola como valor booleano (True/False).
"""
print("f¿La persona forma parte de la unsij?: ",{variable or variable1})