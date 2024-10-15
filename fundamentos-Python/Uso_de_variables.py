# Rosalinda Aquino Pérez
# 14 de octubre  2024
# En este archivo se ejemplifica el uso de variables en Python.
# Notas:
# Variable - una variable es un nombre que almacena un valor guardado en la memoria temporal.

# Toda variable requiere un valor inicial
semestre = 3        # es una variable que almacena un valor de tipo entero
print(semestre)     # imprime el valor de la variable semestre
semestre = 4        # Se modificó el valor de la variable
print(semestre)

nombre = "Rosalinda"  # variable de tipo String
altura = 1.50       # variable de tipo Float
edad = 20           # variable de tipo Int
# Se modificó el valor de la variable
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# Se modifican los valores de las variables y se imprime
altura = 1.60
edad = 22
print()
print("Valores modificados:")
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# En Python, las variables son dinámicas, por lo que pueden almacenar otro tipo de dato en cualquier momento
edad = "treinta y uno" #Se cambió el contenido antes tenia el valor de un entero
print()
print("Edad (con otro tipo de dato):", edad)

# Ejemplos correctos y con buenas prácticas
fecha_nacimiento = "1 de enero del 2000"
clase = "Estructuras de Datos"
horas_estudio = 8
nombre = "Rosalinda"
es_estudiante = True

# Ejemplos incorrectos (líneas comentadas porque marcan error) o de malas prácticas
f = "31 de diciembre del 2003"
fechanacimiento = "31 de diciembre del 2003"
# class = "Estructuras de Datos"
# 8horas_estudio = 8
Nombre = "R o s a l i n d a"
NOMBRE = "ROSALINDA"

# Notar que las variables 'nombre', 'Nombre' y 'NOMBRE', son distintas
print()
print("Las variables son sensibles a mayúsculas y minúsculas:")
print("Variable nombre:", nombre)
print("Variable Nombre:", Nombre)
print("Variable NOMBRE:", NOMBRE)
