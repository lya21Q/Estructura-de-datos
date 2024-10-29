'''
Nombre:Rosalinda Aquino Pérez
Fecha: 28/Octubre/2024
Descripción: Uso de la sentencia de control if - elif - else.
'''

print("Este programa determinará cuál de dos números ingresados por el usuario es menor o si son iguales.")

"""
a) Solicite al usuario dos números decimales.
"""
num1=float(input("Ingrese un número decimal: "))
num2=float(input("ingrese un segundo número decimal"))

"""
b) Utilice la lógica adecuada para determinar cuál de los dos números es menor o si es que son iguales.
"""
if num1 < num2 :
    print("El número uno es menor.")
elif num1 > num2 :
    print("El número dos es menor.")
else :
    print("Son iguales.")
"""
c) Muestre el número menor (o que son iguales) en consola.
"""
print(f"El numero {num1} es menor que {num2}")
