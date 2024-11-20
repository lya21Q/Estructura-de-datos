#Lista de compras
#sum(suma)
#len(cantidad de elemntos)
#1)ver lista
#2)añadir producto a la lista -> nombre/cantidad
#3)eliminar producto
#4)salir

op= None
lista = []
cantidad=0

while op!=4:
    print("* Lista de compras *")
    print("[1].-Ver lista ")
    print("[2].-Añadir producto a la lista ")
    print("[3].-Eliminar producto de la lista ")
    print("[4].-Salir ")
    op = int(input("Ingrese opción:"))

    if op==1:
        indice = 0
        for producto in lista :
            if indice % 2== 0:
                print(f"El nombre es:{producto}")
            else :
                print(f"La cantidad es:{producto}")
            indice+=1
    elif op==2:
        nombre = input("ingrese el nombre del producto:")
        cantidad = int(input("Ingrese la cantidad que desea añadir:"))
        lista.append(nombre)
        lista.append(cantidad)
    elif op==3:
        indice =0
        for producto in lista:
            if producto % 2:
                print()
        indice+=1
        print("Producto eliminado")
    elif op==4:
        print("Saliendo del programa")
    else :
        print("Opción no válida")
