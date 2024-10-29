'''
Nombre:Rosalinda Aquino Pérez
Fecha: 28/Octubre/2024
Descripción: Uso de la sentencia de control if - elif - else.
'''
print("Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario.")
mes=int(input("Ingrese un número que represente al mes: "))
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
print(f"La estacion del mes es : {estacion}")