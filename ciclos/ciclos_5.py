fila= int(input("Ingrese el numero de filas: "))
#3)
contador = fila
asterisco = "*"
for a in range (1,fila+1) :
    espacio = " " * a
    asterisco= "*" * contador
    print(f"{espacio}{asterisco}")
    contador -= 1
print()

contador = 1
asterisco = "*"
for a in range (1,fila+1):
    espacio = " " * a
    asterisco = "*" * contador
    print(f"{asterisco}{espacio}")
    contador += 1
print()