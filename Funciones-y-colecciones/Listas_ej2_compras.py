'''
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción:
Ejemplos de uso de las Tuplas.
'''
#Lista de compras
#sum(suma)
#len(cantidad de elemntos)
#1)ver lista
#2)añadir producto a la lista -> nombre/cantidad
#3)eliminar producto
#4)salir

op= None#Variable que controla las opciones.
productos = []#LLista 1
cantidades = []#Lista 2
while op!=4:
    #Muestra un menú al usuario.
    print("* Lista de compras *")
    print("[1].-Ver lista ")
    print("[2].-Añadir producto a la lista ")
    print("[3].-Eliminar producto de la lista ")
    print("[4].-Salir ")
    op = int(input("Ingrese opción:"))
    #Caso para ver la lista de productos.
    if op==1:
        indice = 0
        contador=0
        for producto in productos :
            print((f"la cantidad es: {cantidades[contador]}, y los productos es: {producto}. "))
            contador+=1
    #Caso para añadir productos a la lista.
    elif op==2:
        nombre = input("ingrese el nombre del producto:")
        cantidad = int(input("Ingrese la cantidad que desea añadir:"))
        productos.append(nombre)
        cantidades.append(cantidad)
    #Caso para eliminar productos a la lista.
    elif op==3:
        nombre_producto=input("Ingrese el nombre del producto que desea eliminar:")
        numero_producto=0
        while productos[numero_producto]!=nombre_producto:
            cantidades+= 1
        productos.remove(nombre_producto)
        del cantidades[numero_producto]
        print("Producto eliminado")
    elif op==4:
        print("Saliendo del programa")
    else :
        print("Opción no válida")
