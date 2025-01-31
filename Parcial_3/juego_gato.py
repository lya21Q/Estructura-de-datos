#Rosalinda Aquino perez
from random import random, choice, randint

op=None
jugador=None
jugador=None
tablero=[]

#Muestra el yablero
def mostrar_tablero():
    for fila in tablero:#ciclo que itera sobre cada fila del tablero.
        print('-------------')
        for posicion in fila:#ciclo que itera cada columna del tablero
            print('|',posicion,'',end='')
        print('|')
    print("-------------")
    return tablero

columna=[]
fila=[]
for i in range(1,10):#Bucle para crear nuestra lista
    fila.append(i)#Añadir el numero a la fila.
    if i%3==0:
        columna.append(fila)
        fila=[]#Receteamos la fila
tablero=columna[:]

#Funcion para encontral al ganador del juego.
def ganador_juego(tablero):
    ganador=None
    for i in range(3):
        #Comprobar filas
        if tablero[i][0]==tablero[i][1]==tablero[i][2]==tablero[i][0]!='':
            ganador=tablero[i][0]
        #comprueba columnas
        if tablero[i][0]==tablero[1][i]==tablero[2][i]==tablero[0][i]!='':
            ganador=tablero[0][i]
        #Revisar diagonales.
        if tablero[0][0]==tablero[1][1]==tablero[2][2]==tablero[0][0]!='':
            ganador=tablero[i][0]
        if tablero[0][2]==tablero[1][1]==tablero[2][0]==tablero[0][2]!='':
            ganador=tablero[0][2]
        return ganador

# Verifica si una casilla está ocupada.
def casilla_ocupada(tablero,fila,columna, jugador):
    if tablero[fila][columna] == 'X' or tablero[fila][columna] == 'O':
        print("Casilla ocupada.")
    else:
        tablero[fila][columna] = jugador

def menu():
    print("1) X ")
    print("2) O ")
    print("3) salir ")
    op=int(input("Elige una opción:"))
    return op

jugador=None
while op!=3:
    mostrar_tablero()
    lista=[]
    op=menu()
    if jugador=='X':
        fila=int(input("Ingrese la posición de la fila"))
        columna=int(input("Ingrese la posición de la fila"))
    else:
        fila=int(input("Ingresa el numero de posicion de la fila"))
        columna=int(input("Ingresa el numero de posicion de la fila"))


jugador1=int(input("Ingrese una opcion para el jugador 1:"))
jugador2=int(input("Ingrese una opcion para el jugador 2:"))

