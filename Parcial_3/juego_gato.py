#Rosalinda Aquino perez
import random

#Muestra el yablero
def mostrar_tablero():
    for fila in tablero:#ciclo que itera sobre cada fila del tablero.
        print('-------------')
        for j in fila:#ciclo que itera cada columna del tablero
            print('|',j,'',end='')
        print('|')
    print("-------------")
    return tablero

# Verifica si una casilla está ocupada.
def casilla_ocupada(tablero, posicion, jugador):
    fila = posicion // 3
    columna = posicion % 3
    if tablero[fila][columna] == 'X' or tablero[fila][columna] == 'O':
        print("Casilla ocupada.")
    else:
        tablero[fila][columna] = jugador


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


columna=[]
fila=[]
for i in range(1,10):#Bucle para crear nuestra lista
    fila.append(i)#Añadir el numero a la fila.
    if i%3==0:
        columna.append(fila)
        fila=[]#Receteamos la fila

jugador = 'X'
tablero = columna[:]
contador =None

# Bucle principal del juego
while contador != 9:
    mostrar_tablero()  # Mostrar el tablero actual
    if jugador == 'X':  # Si es el turno del jugador
        fila = int(input("Ingrese la fila (0-2): "))
        columna = int(input("Ingrese la columna (0-2): "))
    else:  # Si es el turno de la CPU
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if tablero[fila][columna] == ' ':
            print(f"La CPU elige la posición: ({fila}, {columna})")
            break

    if tablero[fila][columna] == ' ':
        if casilla_ocupada(tablero, fila, columna, jugador):
            ganador = ganador_juego(tablero)
            if ganador:
                mostrar_tablero()
                print(f"¡Jugador {ganador} ha ganado!")
                break
            jugador = 'O' if jugador == 'X' else 'X'  # Cambiar de jugador
            contador += 1
    else:
        print("Posición ocupada, intenta de nuevo.")
