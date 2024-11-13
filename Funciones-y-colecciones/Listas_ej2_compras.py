#Lista de compras
#sum(suma)
#len(cantidad de elemntos)
#1)ver lista
#2)añadir producto a la lista -> nombre/cantidad
#3)eliminar producto
#4)salir

def menu ():
    print("* Lista de compras *")
    print("[1].-Ver lista ")
    print("[2].-Añadir producto a la lista ")
    print("[3].-Eliminar producto de la lista ")
    print("[4].-Salir ")
    op=int(input("Ingrese opción:"))
    return op

def lista (op,nombre1, cantidad,resultado):
    if op==1:
        len(lista)
        print(lista)
    if op==2:
        pro = input("Ingrese nombre de producto: ")
        lista.append(pro)
        cantidad = int(input("Ingese la cantidad que deseea añadir:"))
        cantidad.append(cantidad)
    if op==3:
        print()
    if op==4:
        print()
    else :
        print("Opción no válida")

    return resultado

lista=[]
lista2=[]
op=menu()
