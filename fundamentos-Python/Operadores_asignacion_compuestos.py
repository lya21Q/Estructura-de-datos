'''
Nombre:Rosalinda Aquino Pérez
Fecha:28/Octubre/2024
Descripción:Ejemplos de uso de los operadores de asignación compuestos.
'''

"""
Los operadores de asignación compuestos son una forma abreviada de realizar una operación aritmética y una asignación
en una sola línea de código. Combinan un operador aritmético (como suma, resta, multiplicación, división, etc.) 
con el operador de asignación (=).
"""

numero = int(input("Ingresa un número: "))#Se muestra un mensaje en pantalla, solicitando un número al usuario, esté valor es recibido como tipo cade, y lo convierte a entero y se almacena en la variable número.
print(f"Valor ingresado: {numero}")#Muestra en pantalla el valor de la variable número.

numero+=20 # Se realiza una suma al contenido de la variable número y se almacena en la misma.
print(f"Nuevo valor (+20): {numero}")#Se muestra en pantalla el contenido de la variable número.

numero-=4  # Se realiza una resta al contenido de la variable número y se almacena en la misma.
print(f"Nuevo valor (-4): {numero}")#Se muestra en pantalla el contenido de la variable número.

numero*=2   # Se realiza una resta al contenido de la variable número y se almacena en la misma.
print(f"Nuevo valor (*2): {numero}")#Se muestra en pantalla el contenido de la variable número.

numero/=5     # Se realiza una resta al contenido de la variable número y se almacena en la misma.
print(f"Nuevo valor (/5): {numero:.2f}")#Se muestra en pantalla el contenido de la variable número.


# Ejemplo. ¿Qué se obtiene cuando los números ingresados son 8 y 7?
print()
numero1 = int(input("Ingresa un número: "))#Se muestra un mensaje en pantalla, solicitando un número al usuario, esté valor es recibido como tipo cadena, y lo convierte a entero y se almacena en la variable número.
numero2 = int(input("Ingresa otro número: "))#Se muestra un mensaje en pantalla, solicitando un segundo número al usuario, esté valor es recibido como tipo cadena, y lo convierte a entero y se almacena en la variable número.

numero1 += numero2 #Se suma el contenido de numero1 con numero2, y se guarda en numero1.
numero1 += 2 # Se le suma 2 al contenido de numero1, y se almacena en el mismo.
numero1 *= 5 # Se multiplica el contenido de numero1 por 5, y se almacena en el mismo.
numero2 -= 3 # Se resta 3 al contenido de numero2, y se almacena en el mismo.
numero1 /= numero2 # Se divide numero1 entre numero2 y el resultado se guarda en numero1.


print(f"Resultado de las operaciones sobre el primer número: {numero1}")#Muestra el resultado de las operaciones realizadas al contenido de la variable numero1.
print(f"Resultado de las operaciones sobre el segundo número: {numero2}")#Muestra el resultado de las operaciones realizadas al contenido de la variable numero2.