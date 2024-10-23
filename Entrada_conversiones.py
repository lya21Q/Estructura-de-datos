'''
Nombre:Rosalinda Aquino Pérez.
Fecha:21 de Octubre de 2024.
Descripción: Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Comentar sobre las funciones anidadas.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")
semestre = int(input("Ingresa el no. de semestre: "))
promedio = float(input("Ingresa el promedio: "))
es_mujer = input("¿Es mujer (Si/No)?: ")
# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")