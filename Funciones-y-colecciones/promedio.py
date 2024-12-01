'''
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción:
Ejemplos de uso de las Tuplas.
'''
#1) ver calificaciones del alumno
#2)ver promedios del alumno
#3)añadir alumno
#4)eliminar alumno
#5)ver promedio grupal
#salir

op=None
calificaciones=[]
promedio=[]
def menu():
    print("* Lista de compras *")
    print("[1].-Ver calificaciones del alumno ")
    print("[2].-ver promedios del alumno ")
    print("[3].-Añadir alumno")
    print("[4].-Salir ")

    op = int(input("Ingrese opción:"))

    return op

while op!=4:
    if op==1:
        calificaciones=["nombre"]
        print()
    elif op==2:
        print()
    elif op==3:
        nombre=input("Ingrese el nombre del alumno:")

        nombre.append(nombre)
        print()
    elif op==4:
        print()
    else:
        print("Opción no válida")