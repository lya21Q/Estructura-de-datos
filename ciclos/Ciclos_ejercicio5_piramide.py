fila=int(input("Ingrese el número de filas :"))
asteriscos = "*"

#1)
for i in  range (1,fila+1) :
    asteriscos = "*" * i
    print(f"{asteriscos}")
print()

#2)
asteriscos = "*"
for x in  range (1,fila+1) :
    asteriscos =  "*" * fila
    fila = fila - 1
    print(f"{asteriscos}")

#3)
filas = int(input("Ingrese el número de filas: "))
for i in range(1, filas + 1):
    print(' ' * (filas - i) + '*' * (2 * i - 1))


