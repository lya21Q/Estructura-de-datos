'''
Nombre:Rosalinda Aquino Pérez.
Fecha:21 de Octubre de 2024.
Descripción: Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Comentar sobre las funciones anidadas.
print("****   Datos de los alumnos    *****")#Muestra un mensaje.
nombre = input("Ingresa el nombre: ")#Muestra un mensaje solicitando a que el usuario ingrese su nombre.
semestre = int(input("Ingresa el no. de semestre: "))#Muestra un mensaje solicitando a que el usuario ingrese su semestre.
promedio = float(input("Ingresa el promedio: "))#Muestra un mensaje solicitando a que el usuario ingrese su promedio.
es_mujer = input("¿Es mujer (Si/No)?: ")#Muestra un mensaje de pregunta, sobre si es hombre, o mujer.
# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")#Con la función f muestra el valor de las variables, los datos del alumno.
#{promedio:.2f} convierte el valo de la variable a un número decimal.