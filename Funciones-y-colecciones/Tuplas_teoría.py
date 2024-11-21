'''
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción:
Ejemplos de uso de las Tuplas.
'''

"""
Una tupla es una colección ordenada e inmutable de elementos. Esto significa que:
 - Ordenada: Los elementos se almacenan en un orden específico, y cada elemento tiene un índice asociado.
 - Inmutable: Una vez creada, no se puede agregar, eliminar o cambiar elementos dentro de una tupla.
 - Heterogénea: Una tupla puede contener elementos de diferentes tipos de datos.

Sintaxis para crear una lista:
Se encierra los elementos entre paréntesis () y se separan por comas. 
Nota: el uso de los paréntesis es opcional.

"""

# Primer ejemplo de una tupla
print("  ***  Ejemplo de uso de una Tupla  ***")
fechas_nacimiento = ("2019-10-01", "2020-10-01", "2020-12-01", "2021-06-12", "2022-10-01", "2023-11-01")

print(f"Ejemplo de tupla: {fechas_nacimiento}")     # Se imprime toda la tupla.

print("Se imprime la tupla elemento por elemento:")
for fecha in fechas_nacimiento:     # Se imprime un elemento individual, de la misma forma que con ua lista.
    print(f"{fecha}", end = ", ")

print()
print()


# Ejemplo con la serie de Pi de Leibniz
print("  ***  Serie de pi de Leibniz  ***")

pi_serie = (4, -4/3, 4/5, -4/7, 4/9, -4/11, 4/13, -4/15, 4/17, -4/19, 4/21, -4/23)
print(f"Serie de Leibniz: {pi_serie}")

# La función sum() suma los elementos del parámetro que recibe.
print(f"El número Pi considerando los primeros 3 elementos es: {sum(pi_serie[0:2])}")
print(f"El número Pi considerando los primeros 5 elementos es: {sum(pi_serie[0:4])}")
print(f"El número Pi considerando los primeros 9 elementos es: {sum(pi_serie[0:8])}")
print(f"El número Pi considerando todos los elementos ({len(pi_serie)}) es: {sum(pi_serie)}")
print()


# Ejemplo con coordenadas.
print("  ***  Coordenadas con tuplas  ***")
punto1 = (1, 0)
punto2 = (5, 3)

print(f"Coordenadas en tupla (x, y): {punto1} y {punto2}")

# Desempaquetado de tuplas. Se asignan los valores de la tupla a varias variables.
# En este caso, para calcular una expresión de la recta.
x1, y1 = punto1
x2, y2 = punto2

# Se calcula la pendiente y el offset de la recta.
pendiente = (y2 - y1)/(x2 - x1)
b = y1 - pendiente*x1

print(f"Expresión de la recta: y = {pendiente}*x + {b}")