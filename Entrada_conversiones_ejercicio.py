#Escribe un programa de nombre Entrada_conversiones_ejercicio.py que realice lo siguiente:

'''
Nombre:Rosalinda Aquino Pérez.
Fecha:21 de Octubre de 2024.
Descripción: Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''
#a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:
#Nombre (cadena).
print("***   Datos de los profesores   ***")
nombre = input("Ingresa el nombre: ")
Num_cubo = int(input("Ingrese el No. de cubículo: "))
H_clase = float(input("Ingrese las horas que imparte clase a la semana:  "))
tiempo_en_la_unsij = input("¿Tiene más dde 5 años en la unsij (Si/No)?: ")
#b) Muestre los datos en consola de forma adecuada.
print()
print(f"El profesor {nombre}, tiene como número de cubículo: {Num_cubo}, las horas que imparte clase a la semana son: {H_clase:.3f}. Además, tiene más de 5 años en la unsij: {tiempo_en_la_unsij}.")
#Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera.
