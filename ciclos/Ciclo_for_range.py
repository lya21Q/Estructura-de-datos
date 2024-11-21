'''
Nombre:Rosalinda Aquino Pérez
Fecha:21/11/2024
Descripción:
Uso de la función range en el ciclo for.
'''

"""
la función range() genera una secuencia de números enteros. 
Es especialmente útil cuando se combina con los bucles for para iterar sobre una serie de valores.

Sintaxis básica:
range(número_inicio, número_final, incremento)

en donde:
numero_inicio: (opcional) El número inicial de la secuencia. Por defecto es 0.
numero_final: El número final de la secuencia.
incremento: (opcional) El incremento entre cada número. Por defecto es 1. El número puede ser negativo.
"""

# Primer ejemplo de uso de la función range. Se imprimen los valores del 0 al 4.
print("Los números del 0 al 5 son:")
for i in range(5):
    print(i, end = " ")
print()
print("---------------------------------------------------")
print()

# Segundo ejemplo. Se imprimen los valores del 1 hasta un número ingresado por consola.
numero_final = int(input("Ingresa el número final de la cuenta: "))
print(f"Los números del 1 al {numero_final} son:")
for i in range(1, numero_final + 1): # El incremento de 1 es para mostrar el número final.
    print(i, end=" ")
print()
print("---------------------------------------------------")
print()

# Ahora se imprimen los números pares del 0 hasta un número ingresado por consola.
numero_final = int(input("Ingresa el número final de la cuenta de números pares: "))
print(f"Los números pares del 0 a {numero_final} son: ")
for i in range(0, numero_final + 1, 2): # En lugar de utilizar un if, manejamos incrementos de 2.
    print(i, end=" ")
print()
print("---------------------------------------------------")
print()

# Finalmente, se genera un correo con un índice una cantidad determinada por el usuario.
correo = input("Ingresa el nombre del correo a generar: ")
numero_final = int(input("Ingresa el número de correos a generar: "))
print("La lista de los correos con la primera forma es la siguiente:")
for i in range(numero_final):
    print(f"{correo}{i + 1}@gmail.com")     # Primera forma, incrementando el índice porque por defecto es 0.

print()
print("Con otra forma se obtiene el mismo resultado:")
for i in range(1, numero_final + 1):        # Segunda forma, iniciando en 1 hasta el número más uno.
    print(f"{correo}{i}@gmail.com")