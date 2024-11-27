'''
Nombre:Rosalinda Aquino Pérez
Fecha:21/11/2024
Descripción:Uso del ciclo for.
'''
"""
El ciclo for se utiliza para iterar sobre una secuencia (como una lista, tupla o cadena) y ejecutar un bloque de código 
para cada elemento de esa secuencia.

Sintaxis:
for variable in secuencia:
    # Código a ejecutar con el valor de la variable dentro de la secuencia.

# Nota: Nuevamente, no hay llaves, sino que se deja un espacio. 
"""

# Ejemplo del ciclo for
print("  ***  Ejemplo del ciclo for  ***")
cadena = input("Ingresa una frase: ")  # En este caso, la cadena es la secuencia.

print("Frase con el bucle for:")
# Tomamos un valor en particular (carácter) de toda la secuencia (cadena)
for caracter in cadena:
    print(caracter)

print("Frase con el ciclo for con personalización de la función print():")
for caracter in cadena:
    print(caracter, end=" ")  # El "end =" controla el carácter que se imprime al final de la función print()

# Otro ejemplo con el ciclo for. Imprime los alumnos
alumnos = ["Alumno1", "Alumno2", "Alumno3"]

print()
print("  ***  Segundo ejemplo del ciclo for  ***")
for alumno in alumnos:
    print(f"Hola {alumno}.")