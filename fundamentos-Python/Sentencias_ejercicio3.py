'''
Nombre:Rosalinda Aquino Pérez
Fecha: 28/Octubre/2024
Descripción: Programa que determina un descuento en compras.
'''
print("Este programa determinará un descuento en compras en 'La cona'. ")
compra = float(input("Ingrese la cantidad de compra : "))

membresia= input("Cuenta con menbresía (Si/No): ")
membresia=membresia.lower() == "si"

descuento =0

if membresia == "si" :
    print("Tu descuento es del 5%")
    descuento= compra *0.05
elif membresia =="si" and compra >= 1000 :
    print("Tu descuento es del 8%")
    descuento= compra * 0.08
else :
    print("Se te invita a ser miembro de la tienda y obtener un descuento de hasta el 8%")
print()

total = compra - descuento
print(f"El descuento es {descuento}")
print(f"total a apagar es {compra}")
