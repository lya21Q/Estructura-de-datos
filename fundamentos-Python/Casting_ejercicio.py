#Rosalinda Aquino Pérez
#14 octubre del 2024
#Conversión de tipos de datos.

#a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.
var_float= 3.14159265
var_int = 12
var1_int = 0
print()
print("Conversion de número a cadena")
print(f"Los numeros {var_float}, {var_int}, y {var1_int} se convierten a cadena de la siguiente forma: {str(var_float)}, {str(var_int)}, y {str(var1_int)}.")
print()

#b) De los números anteriores, indica su valor booleano.
print("Conversion a valor booleano")#Imprime un letrero
var_float= 3.14159265
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")
var_int = 12
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")
var1_int = 0
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")
print()

#c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".
var_cadena = "10002"
var_int = int(var_cadena)

var1_cadena = "100.02"
var1_float = float(var1_cadena)

var2_cadena = "0"
var2_bool = bool(var2_cadena)

# Se utiliza la letra "f" antes de las comillas para indicar que la cadena será formateada.
# Se pueden incluir variables y expresiones dentro de las llaves.
print("Conversión de cadena a entero.")# Imprime un letrero
print(f"Número como cadena: {var_cadena}.")
print(f"Número como int más uno: {var_int + 1}.")
print(f"Número como cadena: {var1_cadena}.")
print(f"Número como int más uno: {var1_float + 1}.")
print(f"Número como cadena: {var2_cadena}.")
print(f"Número como int más uno: {var2_bool + 1}.")
print()

#d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".
print("Conversion a valor booleano")
var_cadena = "10002"
es_verdadero = bool(var_cadena)#se declara el la variable bool
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")

var1_cadena = "100.02"
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")

var2_cadena = "0"
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")
print()