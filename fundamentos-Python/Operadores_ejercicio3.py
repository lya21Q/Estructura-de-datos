
print("Escribe un programa de nombre Operadores_ejercicio3.py que realice lo siguiente")
print("Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña.")
"""
'''
Nombre:Rosalinda Aquino Pérez
Fecha:28/Octubre/2024
'''

a) Internamente declare dos cadenas constantes, una para el usuario y otra para la contraseña.
"""
usuario1= "alumnos"
contrasena1= "python"
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
variable = (usuario1 == usuario) and (contrasena1 == contrasena)

"""
e) Muestre el resultado en consola como valor booleano (True/False).
"""
print(f"La revisión fue correcta: {variable}")