#Rosalinda Aquino Pérez
#Descripción del programa: Este programa imprime una pirámide de caracteres '*' de cuatro formas:
"""
1)
*
**
***

2)
***
**
*

3)
  *
 ***
*****

4)
  *
 **
***
###
"""
#Solicita al usuario que ingrese el numero de filas.
fila=int(input("Ingrese el número de filas :"))
asteriscos = "*"

#1)Caso 1
for i in range (1,fila+1) :
    asteriscos = "*" * i
    print(f"{asteriscos}")
print("--------------------------")

#2)Caso 2
for i in range (fila,0,-1) :
    asteriscos = "*" * i
    print(f"{asteriscos}")
print("---------------------------------------")

#3) Caso 3
for z in range(1, fila + 1):
    print(' ' * (fila - z) + '*' * (2 * z - 1))
print("-----------------------------------------")
#4) Caso 4
for i in range (1,fila+1):
        espacios = ' ' * (fila -i )
        asteriscos = espacios + "*" * i
        print(f"{asteriscos}")
print("-------------------------------------")

