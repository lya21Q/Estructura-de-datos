'''
Nombre:Rosalinda Aquino Pérez
Fecha: 28/Octubre/2024
Descripción: Uso de la sentencia de control if - elif - else.
'''
"""
La sentencia elif es una extensión del if-else y permite evaluar múltiples condiciones de forma secuencial. 
Es como tener varias opciones a elegir, ejecutándose el bloque de código correspondiente a la primera condición 
que sea verdadera.
Sintaxis:
if condicion_1:
    # Código a ejecutar si la condición_1 es verdadera.
elif condición_2:
    # Código a ejecutar si la condición_2 es verdadera.
  .
  .
  .
else:
    # Código que se ejecuta si todas las condiciones fueron falsas.
"""

print("  ***  Programa que determina el grupo de acuerdo a la edad  ***")#Imprime un mensaje en pantalla.
edad = int(input("Ingresa tu edad: "))#Solicita su edad al usuario.

# ocupamos la condicional if-elif-else para determinar a que grupo pertenece de acuerdo a la edad ingresada.
if edad < 14:#Si la edad es menor que 14, se asigna el valor "Niños y adolescentes"
    grupo = "Niños y adolescentes"

elif 15 <= edad < 25:#Si la edad es menor o igual a 14, y menor a 25 se asigna el valor "Jóvenes" a ala variable grupo.
    grupo = "Jóvenes"

elif 25 <= edad < 45:#Si la edad es menor o igual a 25, y menor a 45 se asigna el valor "Adultos jóvenes" a ala variable grupo.
    grupo = "Adultos jóvenes"

elif 45 <= edad < 60:#Si la edad es menor o igual a 45, y mayor a 60 se asigna el valor "Adultos Maduros" a ala variable grupo.
    grupo = "Adultos maduros"

else:
    grupo = "Adultos mayores" #Si ninguna de las condiciones fue verdadera, entonces se le asigna el valor de "Adultos mayores", a la variable grupo.

print(f"El grupo al que perteneces es: {grupo}.")#Se imprime el resultado obtenido.

