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
    return [[" " for _ in range(3)] for _ in range(3)]

#Muestra el yablero
def mostrar_tablero(tablero):
    print("   1   2   3")
    for i, fila in enumerate(tablero):
        print(f"{i + 1}  " + " | ".join(fila))
        if i < 2:
            print("  -----------")

def colocar_ficha (tablero,columna,fila,ficha):
    if tablero[fila-1][columna-1]==" ":
        tablero[fila-1][columna-1]=ficha
        return True
    return False

def ganador_juego(tablero,ficha):

    for i in range(2):
        #Comprobar filas
        if tablero[i][0]==ficha and tablero[i][1]==ficha and tablero[i][2]==ficha :
            print(f"Gano {ficha}")
            return False
        #comprueba columnas
        if tablero[0][i]==ficha and tablero[1][i]==ficha and tablero[2][i]==ficha:
            print(f"Gano {ficha}")
            return False
        #Revisar diagonales.
    if tablero[0][0]==ficha and tablero[1][1]==ficha and tablero[2][2]==ficha:
        print(f"Gano {ficha}")
        return False
    if tablero[0][2]==ficha and tablero[1][1]==ficha and tablero[2][0]==ficha:
        print(f"Gano {ficha}")
        return False

    return True

# ///////////////////////////////////////////////////////////////////////////////////////// Función main.
def main ():
    contador =0
    tablero = crear_tablero_gato()
    # Bucle principal del juego
    ficha = "X"
    op=menu()
    while contador < 9 and ganador_juego(tablero,ficha):
        contador+=1
        mostrar_tablero(tablero)  # Mostrar el tablero actual
        if op== 1:
            if contador % 2 == 1:
                columna = int(input("Ingresa el numero de columna:"))
                fila = int(input("Ingresa el numero de fila:"))
                ficha = "X"
                colocar_ficha(tablero, columna, fila, ficha)
                print(f"Gano {ficha}")
            else:
                columna = int(input("Ingresa el numero de columna: "))
                fila = int(input("Ingresa el numero de fila: "))
                ficha = "0"
                colocar_ficha(tablero, columna, fila, ficha)
        elif op==2:
            if contador % 2 == 0:
                columna = int(input("Ingresa el numero de columna: "))
                fila = int(input("Ingresa el numero de fila: "))
                ficha = "X"
                colocar_ficha(tablero, columna, fila, ficha)
            else:
                columna = random.randint(0, 3)
                fila = random.randint(0, 3)
                ficha = "O"
                colocar_ficha(tablero, columna, fila, ficha)
            if contador==9:
                print("¡Empate!")

if __name__ == "__main__":
    main()