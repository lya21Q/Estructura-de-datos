"""
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción:
Ejercicio 1.
"""
op=None
#Muestra el menú al usuario.
print("Este programa almacena diversos puntos como coordenadas y permite obtener la ecuación de la recta entre dos de los puntos.")
def menu():
    print("[1] Ver cordenadas")
    print("[2] Agregar coordenada")
    print("[3] Calcular la pendiente y la ecuación de la recta entre dos corrdenadas.")
    print("[4] Eliminar coordenada")
    print("[0] Salir")
    #Solicita al usuario que ingrese una opción.
    op=int(input("Ingrese una opcion: "))
    return op

coordenada_X=0
coordenada_Y=0
tupla=()
coordenadas=[]

while op!=0:
    op=menu()
    if op==0:
        print("Saliendo del programa.")
    elif op == 1:
        if len(coordenadas)!=0:
            print(f"La lista de números es: {coordenadas}")
        else:
            print("No hay valores que mostrar.")
    elif op == 2:
        coordenada_X=float(input("Ingrese coordenada X"))
        coordenada_Y=float(input("Ingrese coordenada Y"))
        tupla=(coordenada_X,coordenada_Y)
        coordenadas.append((tupla))
        print(f"La coordenada {coordenada_X,coordenada_Y} se agrego con éxito!. ")
    elif op == 3:
        if len(coordenadas)!=0:
            print("No se puede calcular la pendiente.")
        else:
            numero=+1
            indice1_=int(input("Ingrese el indice de la primera coordenada:"))
            indice2_=int(input("Ingrese el indice de la segunda coordenada:"))
            coordenada_x1,coordenada_Y1=(coordenadas[indice1_])
            coordenada_X2,coordenada_Y2=(coordenadas[indice2_])
            #Pendiente : y=mx+b
            m=(coordenada_Y2-coordenada_Y1)/(coordenada_X2-coordenada_x1)
            b=coordenada_Y1-m*coordenada_x1
            print(f"La pendiente es {m}")
            print(f"Expresión de la recta es: y={m}x+({b}")
    elif op == 4:
        if len(coordenadas)!=0:
            eliminar=int(input("Ingrese el indice de la coordenada que quiera eliminar."))
            del coordenadas[eliminar]
        else:
            print("No hay coordenadas para eliminar.")
    else:
        print(" Opción incorrecta.")
