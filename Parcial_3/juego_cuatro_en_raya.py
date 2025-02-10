#Rosalinda Aquino perez
import random

def menu():
        """

        :return: retorna un valor entero según haya elegido el usuario.
        """
        print("*** Modo de juego ***")
        print("[1].- Jugador contra jugador")
        print("[2].- Jugador con CPU")
        print("[3].- Salir")
        opcion = input("Selecciona una opción: ")
        while not opcion.isnumeric() or int(opcion) not in range(1, 4):
            print("Opción no válida. Intenta de nuevo")
            opcion = input("Selecciona una opción: ")
        return int(opcion)

def crear_tablero_gato() -> list:
    """
    Crea un tablero vacío de 3 filas por 3 columnas.
    :return: Regresa el tablero en forma de lista.
    """
    return [[" " for _ in range(6)] for _ in range(6)]

#Muestra el yablero
def mostrar_tablero(tablero):
    print(" 1   2   3   4   5   6 ")
    print("-------------------------0")
    for fila in tablero:
        print("|" + "|".join(f" {celda} " for celda in fila) + "|")
        print("-------------------------")

def colocar_ficha (tablero,columna,ficha):
    for fila in reversed(tablero): # Reversed se utiliza para rocesar elementos en orden inverso, en este caso lo uso para recorrer el contenido al revés y rellenar el espacio vacio al fondo de la columna.
        if fila[columna] == " ":
            fila[columna] = ficha
            return True
    return False

def ganador_juego(tablero,ficha):
    for fila in tablero:        # ................................ Verificar filas.
        for col in range(4):
            if all(fila[col + i] == ficha for i in range(4)):
                return True


    for col in range(6):        # ................................ Verificar columnas.
        for fila in range(3):
            if all(tablero[fila + i][col] == ficha for i in range(4)):
                return True


    for fila in range(3):       # ................................ Verificar diagonales hacia abajo.
        for col in range(4):
            if all(tablero[fila + i][col + i] == ficha for i in range(4)):
                return True


    for fila in range(3, 6):    # ................................ Verificar diagonales hacia arriba.
        for col in range(4):
            if all(tablero[fila - i][col + i] == ficha for i in range(4)):
                return True

    return False

# ///////////////////////////////////////////////////////////////////////////////////////// Función main.
def main():
    contador =0
    tablero = crear_tablero_gato()
    op=menu()
    # Bucle principal del juego
    ficha = "X"
    while contador!=20:
        contador+=1
        mostrar_tablero(tablero)  # Mostrar el tablero actual
        if op== 1:
            if contador % 2 == 1 and contador <= 42:
                columna = int(input("Ingresa el numero de columna"))
                ficha = "X"
                colocar_ficha(tablero, columna, ficha)
            if contador % 2 == 0 and contador <= 42:
                columna = int(input("Ingresa el numero de columna"))
                ficha = "0"
                colocar_ficha(tablero, columna,ficha)

        if op==2:
            if contador % 2 == 1 and contador <= 42:
                columna = int(input("Ingresa el numero de columna"))
                ficha = "X"
                colocar_ficha(tablero, columna,ficha)
            if contador % 2 == 0 and contador <= 42:
                columna = random.randint(0, 5)
                ficha = "O"
                colocar_ficha(tablero, columna, ficha)
                print()

        if ganador_juego(tablero,ficha):
            mostrar_tablero(tablero)
            print(f"El ganador es {ficha}")
            break

if __name__=="__main__":
    main()