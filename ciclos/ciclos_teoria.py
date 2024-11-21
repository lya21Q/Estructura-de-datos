'''
Nombre:
Fecha:
Descripción:
Uso del ciclo while.
'''

"""
El ciclo while es una estructura de control fundamental en la programación que permite repetir un bloque de código 
mientras una determinada condición se evalúe como verdadera.

Sintaxis:

while condicion:
    # Código a ejecutar mientras la condición sea verdadera.

# Nota: No hay llaves, sino que se deja un espacio. 
"""

# Ejemplo de uso del ciclo while. Imprimir los números del 1 hasta un número solicitado por consola.
print("  ***  Ejemplo del ciclo while  ***")

numero = int(input("Ingresa un número: "))  # Se solicita un número al usuario.


# Se imprimen los números
print()
print(f"Los números del 1 al {numero} son: ")

contador = 1
while contador <= numero:
    print(contador, end = " ") # El "end =" controla el carácter que se imprime al final de la función print()
    contador += 1

print("Fin de la cuenta.")

# Otro ejemplo del ciclo while. Imprimir los números pares del 0 hasta el número ingresado pro consola.
print()
print("  ***  Otro ejemplo del ciclo while  ***")

numero = int(input("Ingresa otro número: "))

print()
print(f"Los números pares del 0 al {numero} son: ")

contador = 0
while contador <= numero:
    print(contador, end = " ")
    contador += 2

print("\nFin de la cuenta.")        # Notar la diferencia de este print() con el ejemplo anterior.
