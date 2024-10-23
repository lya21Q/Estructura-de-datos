#Nombre:Rosalinda Aquino Pérez
#Fecha: 21 de octubre del 2024
#Descripción: Entrada de datos por consola, valores dinámicos.

numero1_cadena = input("Introduce un número decimal: ")#Muestra un letrero, pidiendo al usuario que ingrese un número decimal.
numero2_cadena = input("Introduce otro número decimal: ")#Muestra un letrero, pidiendo al usuario que ingrese otro número decimal
resultado_cadena = numero1_cadena + numero2_cadena # De los valores que contienen las variables hace una concatenació, las une, con el operador +.
print()
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")#Imprime el resultado de la concatenación.
# Comentar por qué se realiza el casting de variables.
numero1_float = float(numero1_cadena)#Se realiza una conversion de cadena a numeros de tipo float.
numero2_float = float(numero2_cadena)#Se realiza una conversion de cadena a numeros de tipo float.
resultado_float = numero1_float + numero2_float # Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")#Muestra los valores de las conversiones.


print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")#Muestra un letrero, pidiendo al usuario, que ingrese un nombre.
semestre = int(input("Ingresa el no. de semestre: "))#Muestra un letrero, pidiendo al usuario, que ingrese su semestre.
promedio = float(input("Ingresa el promedio: "))#Muestra un letrero, pidiendo al usuario, que ingrese el promedio.
es_mujer = input("¿Es mujer (Si/No)?: ")#Muestra un letrero, preguntando al usuario, si a la persona que agrego es hombre o mujer.
# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")#con la función muestra el valor de las variables, los datos del alumno.
#{promedio:.2f} convierte el valo de la variable a un número decimal.


