#Rosalinda Aquino Pérez
#Descripción del programa: Este programa imprime una pirámide de caracteres '*' de cuatro formas y es la versión del ejercicio Ciclos_ej5_piramide.py, pero ahora utilizando funciones.
#Cada pirámide debe estar en una función, la cual se llama en el código a nivel de módulo de acuerdo a las filas requeridas por el usuario.

asteriscos = "*"
def opcion1(fila):
    print("Forma 1:")
    for i in range (1,fila+1) :
        asteriscos = "*" * i
        print(f"{asteriscos}")
    print("--------------------------")

def opcion2(fila):
    print("Forma 2:")
    for i in range (fila,0,-1) :
        asteriscos = "*" * i
        print(f"{asteriscos}")
    print("---------------------------------------")

def opcion3(fila):
    print("Forma 3:")
    for z in range(1, fila + 1):
        print(' ' * (fila - z) + '*' * (2 * z - 1))
    print("-----------------------------------------")

def opcion4(fila):
    print("Forma 4:")
    for i in range (1,fila+1):
            espacios = ' ' * (fila -i )
            asteriscos = espacios + "*" * i
            print(f"{asteriscos}")
    print("-------------------------------------")


#Solicita al usuario que ingrese el número de filas.
fila=int(input("Ingrese el número de filas :"))
opcion1(fila)
opcion2(fila)
opcion3(fila)
opcion4(fila)