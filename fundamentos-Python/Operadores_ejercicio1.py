"""
Escribe un programa de nombre Operadores_ejercicio1.py que realice lo siguiente:
#Rosalinda Aquino Pérez
#22/Octubre/2024
"""
print("Este programa determinará si el usuario aplica para una bonificación.")
"""
a) Solicite al usuario un número decimal con el valor de una compra.
"""
compra = (float(input("Ingrese un numero decimal: ")))

"""
b) Pregunte al usuario si la compra fue a MSI (Si/No).
"""
compra = input("La compra fue a MSI (Si/No): ")
compra = compra.lower() == "si"
"""
c) El usuario aplica a la bonificación si la compra fue mayor a 5000.00 y si la compra fue a MSI.
"""
if compra >= 5000.00 and compra == "Si" :
    print("Aplica a la bonificación")
"""
d) Muestre el resultado en consola como valor booleano (True/False).
"""
print(f"La compra aplica a la bonificación: ",{compra})