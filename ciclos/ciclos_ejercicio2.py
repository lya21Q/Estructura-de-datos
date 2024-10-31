"""
programa que calcula la suma acumulativa rntre 2 numeros
"""

#ingresa el numero inicial de la cuenta
numero_I=int(input("Ingrese el número inicial: "))
#ingresa el numero final de la cuenta
numero_F=int(input("Ingrese el número final de la cuenta: "))
#la suma de { } hasta { } es

contador = 0
aux = 0
while contador <= numero_F:
    aux += contador
    contador += 1
print(aux)
#funcion randint pide dos valores