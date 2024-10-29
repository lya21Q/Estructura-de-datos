'''
Nombre:Rosalinda Aquino Pérez
Fecha: 28/Octubre/2024
Descripción: Uso de la sentencia de control if - elif - else.
'''
print("Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario.")
'''

a) Solicite al usuario un número que representa al mes.
'''
mes=int(input("Ingrese un número que represente al mes: "))

'''
b) Utilice la lógica adecuada para determinar la estación del año de acuerdo con:
    3, 4 y 5: Primavera.
    6, 7 y 8: Verano.
    9,10 y 11: Otoño.
    12, 1 y 2: Invierno.
    Otro caso: Mensaje de mes incorrecto.
'''
if mes >= 3 and mes <=5  :
    estacion = "Primavera"
elif mes >=6 and mes <=8 :
    estacion = "Verano"
elif mes >=9 and mes  <= 11:
    estacion = "Otoño"
elif mes ==12 or mes == 1 or mes ==2  :
    estacion = "Invierno"
else:
    print("Mes incorrecto")
'''
c) Muestre la estación correspondiente en consola.
'''
print(f"La estacion del mes es : {estacion}")