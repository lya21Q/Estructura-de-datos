#Rosalinda Aquino perez
import random

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
posicion=tablero
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

contador =0
jugador=None
tablero=columna[:]
# Bucle principal del juego

while contador != 9:
    mostrar_tablero()  # Mostrar el tablero actual
    if jugador == 'X': #turno del jugador
        fila=input("Ingresa la posición de la fila:")
        columna=input("Ingresa la posición de la columna:")
    else:
        CPU=random.randint(0,2)
        print("Tiro del CPU")
    if ganador_juego(tablero):
        print(f"El ganador es {jugador}")


