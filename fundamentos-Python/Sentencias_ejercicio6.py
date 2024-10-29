'''
Nombre:Rosalinda Aquino Pérez
Fecha: 28/Octubre/2024
'''
print("Este programa mostrará los detalles del tour turístico Ecoturixtlán de acuerdo a las siguientes tarifas")

nombre= input("Ingrese el nombre de la persona a cargo : ")
Precio_adulto= 200
Precio_nino= 100
numero=int(input("Ingrese el número de adultos: "))
numero1 =int(input("Ingrese el de niños: "))
dia= input("Ingrese el día de la semana: ")

t = (Precio_nino * numero1) + (Precio_adulto * numero)
descuento = 0
if dia ==  "lunes" or "martes" or "jueves" :
    descuento = t * 0.10

total=t-descuento
print()
print(f"Gracias por tu visita {nombre} este dia {dia}. El costo total es de {total}")