'''
Nombre:
Fecha:
Descripción:
Ejemplos de uso de las listas.
'''

"""
Una lista en Python es una colección ordenada y mutable de elementos. Esto significa que:
 - Ordenada: Los elementos se almacenan en un orden específico, y cada elemento tiene un índice asociado.
 - Mutable: Puedes modificar una lista después de su creación, agregando, eliminando o cambiando elementos.
 - Heterogénea: Una lista puede contener elementos de diferentes tipos de datos (enteros, cadenas, flotantes, incluso otras listas).

Sintaxis para crear una lista:
Se encierra los elementos entre corchetes [] y sepáralos por comas.

"""

# Se crea una lista vacía y se imprime.
print("          ********  Ejemplos de uso de listas  ********")

lista_alumnos = []

print(f"Lista vacía: {lista_alumnos}")
print()

# Se añaden elementos al final de la lista y se imprime.
print("Se añaden elementos a la lista.")

lista_alumnos.append("Alberto")
lista_alumnos.append("Alejandra")
lista_alumnos.append("Diego")
lista_alumnos.append("Kike")
lista_alumnos.append("Laura")
lista_alumnos.append("Yaki")
lista_alumnos.append("León")
lista_alumnos.append("Hola")
lista_alumnos.append("Gato")

print(f"Lista con elementos añadidos: {lista_alumnos}")
print()

# Se acceden a los elementos de la lista
print("Se accede a los elementos de una lista.")

print(f"lista_alumno[2] = {lista_alumnos[2]}") # Accedemos al tercer elemento (los índices empiezan con cero).
print(f"lista_alumno[4] = {lista_alumnos[4]}") # Accedemos al quinto elemento.
print()

# Se añaden elementos, pero ahora en un índice específico.
print("Se añaden elementos en un índice específico.")
print(f"Lista antes de añadir un elemento: {lista_alumnos}")

lista_alumnos.insert(2,"Yared")

print(f"Lista después de añadir un elemento: {lista_alumnos}") # Los demás valores se recorren.
print()

# Se modifican los elementos de la lista.
print("Se modifican los elementos en un índice específico.")
print(f"Lista antes de modificar un elemento: {lista_alumnos}")

lista_alumnos[4] = "Enrique"

print(f"Lista después de modificar un elemento: {lista_alumnos}")
print()

# Se eliminan los elementos de la lista. Los elementos se recorren como resultado.
print("Se eliminan los elementos de una lista.")
print(f"Lista antes de eliminar un elemento: {lista_alumnos}")

lista_alumnos.remove("León")        # Se elimina por el valor en la lista.
print(f"Lista eliminando el valor de 'León': {lista_alumnos}")

lista_alumnos.pop(7)                # Se elimina por el índice de la lista.
print(f"Lista eliminando el índice 7 mediante pop: {lista_alumnos}")

del lista_alumnos[7]                # Otra forma de eliminar el elemento.
print(f"Lista eliminando el índice 7 mediante del: {lista_alumnos}")
print()

# Funciones básicas con listas.
print("Funciones básicas que se utilizan en las listas.")
print(f"Tamaño de la lista utilizando la función len(lista_alumnos): {len(lista_alumnos)}")

lista_alumnos.sort()                    # Ordenar la lista por orden ascendente (A-Z).
print(f"Ordenar la lista de manera ascendente utilizando sort: {lista_alumnos}")

lista_alumnos.sort(reverse = True )     # Ordenar la lista por orden descendente (Z-A).
print(f"Ordenar la lista de manera descendente utilizando sort(reverse = True): {lista_alumnos}")
print()

# Acceder a los elementos de la lista utilizando ciclos.
print("Se accede a los elementos individuales de la lista utilizando un ciclo for.")
for alumno in lista_alumnos:
    print(f"Hola {alumno}", end = " - ")