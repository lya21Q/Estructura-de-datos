"""
Escribe un programa de nombre Operadores_ejercicio3.py que realice lo siguiente:

Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña. Para ello:
"""
"""
a) Internamente declare dos cadenas constantes, una para el usuario y otra para la contraseña.
"""
usuario1= "usuario"
contrasena1= "contrasena"
"""
b) Pida al usuario una cadena con el usuario.
"""
usuario = input("Ingrese el nombre de usuario: ")

"""
c) Pida al usuario una cadena con la contraseña.
"""
contrasena = input("Ingrese la contraseña: ")
"""
d) Si ambas cadenas son iguales a las cadenas declaradas internamente, entonces el usario se autenticó correctamente.
"""
variable = (usuario == usuario1) and (contrasena == contrasena1)

"""
e) Muestre el resultado en consola como valor booleano (True/False).
"""
print(f"La revisión fue correcta: {variable}")