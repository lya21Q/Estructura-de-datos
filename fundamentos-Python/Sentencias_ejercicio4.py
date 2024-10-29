'''
Nombre:Rosalinda Aquino Pérez
Fecha: 28/Octubre/2024
'''

print("Este programa determinará si te permiten el acceso al bar 'La Negra'.")

edad=int(input("Ingrese su edad: "))
dinero=int(input("Ingrese la cantidad con la cuenta :"))

if edad >= 18 and dinero >= 250  :
    print("¡Bienvenido a tu mejor bar!")
else :
    print( "Lo sentimos, ya estamos por cerrar!")