"""
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción:
Ejercicio 1.
"""
print("Este programa almacena diversos puntos como coordenadas y permite obtener la ecuación de la recta entre dos de los puntos.")
def menu():
    print("[1] Ver cordenadas")
    print("[2] Agregar coordenada")
    print("[3] Calcular la pendiente y la ecuación de la recta entre dos corrdenadas.")
    print("[4] Eliminar coordenada]")
    print("[0] Salir")
    op=int(input("Ingrese una opcion: "))
    return op
coordenada_X=0
coordenada_Y=0
tupla=(coordenada_X, coordenada_Y)
lista=[tupla]
def coordenadas(op,tupla,lista):
    if op == 1:
        if not tupla:
            print(f"No hay coordenadas para mostrar")
            print()
            print("------------------------------------")
        else:
            for f in lista:
                print("Lista de cooordenadas.")
                print()
                print(f"Cordenada{f+1}: {tupla}")
    elif op == 2:
        coordenada_X=float(input("Ingrese coordenada X"))
        coordenada_Y=float(input("Ingrese coordenada Y"))
        lista.append((coordenada_X, coordenada_Y))
        tupla=(coordenada_X, coordenada_Y)
        print(f"La coordenada {coordenada_X,coordenada_Y} se agrego con éxito!. ")
    elif op == 3:
        if not tupla:
            print(f"No hay coordenadas para mostrar")
            print()
            print("-------------------------------------")
        else:
            print("Lista de cooordenadas.")
    elif op == 0:
        print()
    else:
        print("Saliendo del programa")
    return tupla
op=menu()
tupla=coordenadas(op,tupla,lista)