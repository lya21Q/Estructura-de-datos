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


