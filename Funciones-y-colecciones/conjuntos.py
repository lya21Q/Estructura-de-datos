#Desordenado y mutable: No tiene un indice, pero si puede crecer y modificarse.
"""
*** Ejemplos de uso de conjuntos ***
"""
#lista->[]
#tupla->()
conjunto_nombres=set()#Crear un conjunto vacío
print(f"conjunto vacío: {conjunto_nombres}")
#para añadir valores al conjunto:
conjunto_nombres.add("Rebeca")
conjunto_nombres.add("Juan")
conjunto_nombres.add("Bryann")
conjunto_nombres.add("Jamileth")
conjunto_nombres.add("Scarlett")
conjunto_nombres.add("Rosalinda")
conjunto_nombres.add("Jenny")
conjunto_nombres.add("Tania")
conjunto_nombres.add("Jesus")
conjunto_nombres.add("Patty")
conjunto_nombres.add("Addi")
conjunto_nombres.add("Alberto")
print(f"El conjunto de elementos:{conjunto_nombres}")
print()

"""
*** Conjunto vacío ***
"""
conjunto_nombres.add("Rebeca")
conjunto_nombres.add("Juan")
conjunto_nombres.add("Bryann")
conjunto_nombres.add("Jamileth")
conjunto_nombres.add("Scarlett")
conjunto_nombres.add("Rosalinda")
conjunto_nombres.add("Jenny")
conjunto_nombres.add("Tania")
conjunto_nombres.add("Jesus")
conjunto_nombres.add("Patty")
conjunto_nombres.add("Addi")
conjunto_nombres.add("Alberto")
print(f"El conjunto de elementos:{conjunto_nombres}")
print()
"""
*** Se eliminan elementos del conjunto *** 
"""
conjunto_nombres.remove("Tania")
print(f"ELEMENTOS : {conjunto_nombres}")
print()

"""
***Mostrar elementos ***
"""

for nombre in conjunto_nombres:
    print(nombre, end=" ")
print()

"""
*** Verificar si un elemento pertenece a un conjunto ***
"""
print(f"El elemento  pertenece al conjunto? {'Juan' in conjunto_nombres} ")

"""
nuestro conjunto de numeros ={
"""
conjunto_numeros ={12.1,1.2,302,2.3,4.1}
#Funciones basicas
"""
*** Funciones básicas ***
"""
tamaño_del_conjunto=(conjunto_numeros)
suma_de_todos_los_elementos=sum(conjunto_numeros)
print(suma_de_todos_los_elementos)