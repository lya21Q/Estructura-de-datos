'''
Nombre:Rosalinda Aquino Pérez
Fecha: 28/Octubre/2024
Descripción: Ejemplos de uso de los operadores de asignación.
'''

"""
En programación, las operaciones de asignación se utilizan para almacenar un valor en una variable. 
Es decir, se establece una relación entre un nombre (la variable) y un valor en la memoria de la computadora.
"""
# Asignación múltiple.
print("   ***   Asignación múltiple   ***")
nombre, primer_apellido, segundo_apellido = "Rosalinda", "Aquino", "Pérez" #Se asignan tres valores a tres variables al mismo tiempo.
print(f"Asignación múltiple de cadenas: {nombre} {primer_apellido} {segundo_apellido}")# Se muestran los valores asignados a las tres variables.

entero1, entero2 = 1, 2 # Se asignan dos valores enteros a dos variables al mismo tiempo.
print(f"Asignación múltiple de enteros: {entero1} y {entero2}") #Se imprimen los valores asignados a las dos variables al mismo tiempo.

decimal1, decimal2, decimal3, decimal4 = 3.14, 3.1416, 3.14159, 3.141592 # Se asignan cuatro valores decimales a cuatro variables al mismo tiempo.
print(f"Asignación múltiple de decimales: {decimal1}, {decimal2}, {decimal3} y {decimal4}")# Imprime los valores asignadas a cada variable al mismo tiempo.

# Es posible combinar tipos de datos.
nombre, entero1, decimal4 = "Rosalinda", 12, 3.1415926 #Se asignan valores a tres variables al mismo tiempo combinando diferentes tipos de datos.
print(f"Asignación múltiple: {nombre}, {entero1} y {decimal4}") #Se imprimen los valores asignados a las variables al mismo tiempo.

# Es posible asignar distintas operaciones.
suma, resta = entero1 + entero2, decimal1 - decimal2 #Se realiza una operación distinta y se almacena el resultado a cada variable, al mismo tiempo.
print(f"Asignaciones de operaciones: suma {suma} y resta {resta:.4f}") # Se muestran los resultados de las operaciones realizadas que se habían guardado en cada variable.

# Asignación encadenada.
print()
print("   ***   Asignación encadenada   ***")
entero3 = entero4 = entero5 = 10    # Se les asigna el mismo valor a todas las variables.
print(f"Asignación encadenada de: {entero3} = {entero4} = {entero5} = 10") # Imprime los valores de las variables.

# Intercambio de variables.
print()
print("   ***   Intercambio de variables   ***")
entero5, entero6 = 5, 6 #Se asinan valores a cada variable, al mismo tiempo.
print(f"Valores asignados: entero5 = {entero5} y entero6 = {entero6}")#Imprime un letrero seguido de los valores asignados a las variables.
entero6, entero5 = entero5, entero6 # Se intercambian los valores de las variables.
print(f"Valores intercambiados: entero5 = {entero5} y entero6 = {entero6}") # Imprime un letrero seguido de los valores ya intercambiados anteriormente.

variable_prueba1, variable_prueba2 = 100, "Hola mundo" #Se asignan valores de distinto tipo de dato a las variables al mismo tiempo.
# Es posible porque las variables son dinámicas.
variable_prueba1, variable_prueba2 = variable_prueba2, variable_prueba1 #Se hace el intercambio de valores a las variables.
print(f"Valores asignados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}") #Se muestra los valores asignados a cada variable.
print(f"Valores intercambiados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}") #Se muestran los valores ya intercambiados de cada variable.