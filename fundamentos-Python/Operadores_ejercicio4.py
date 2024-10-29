print("Escribe un programa de nombre Operadores_ejercicio4.py que realice lo siguiente")
print("Este programa determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4)")
"""
a) Pida al usuario cuatro valores booleanos (V/F).
"""
valor= input("Ingrese un vaalor (si/no): ")
valor1 = input("Ingrese un vaalor (si/no): ")

"""
b) Obtenga el resultado de la expresión booleana de acuerdo con los valores ingresados.
"""
valor=valor.lower()== "si"
valor1=  valor1.lower()== "si"
"""
c) Muestre el resultado en consola como valor booleano (True/False).
"""
print(f"El resultado del primero valor es: {valor}")
print(f"El resultado del segundo valor es: {valor1}")