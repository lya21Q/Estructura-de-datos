from random import random, choice

#Inicialización de variables del programa.
op = None #Opción del menú seleccionada por el jugador.
Victorias_del_jugador = 0 #Contador de las  victorias del jugador.
Empates = 0 #Contador de empates.
Victorias_del_CPU = 0  #Contador de las victorias del CPU.

#Constantes para las opciones del juego y los resultados.
PIEDRA = "Piedra."
PAPEL = "Papel."
TIJERA = "Tijera."
JUGADOR = "Gana el jugador."
EMPATE = "Empate."
CPU = "Gana la CPU."
#Función que muestra el menú y devuelve la opción seleccionada por el jugador.
def menu():
    print("  ***  Juego de piedra, papel o tijeras  ***")
    print(f"Victorias del jugador: {Victorias_del_jugador}, empates: {Empates} y victorias del CPU: {Victorias_del_CPU}  ")
    print("[1].- Piedra.")
    print("[2].- Papel.")
    print("[3].- Tijera.")
    print("[4].-Salir.")
    print()
    op = int(input("Ingresa una opción: "))
    return op

#Función que realiza la elección del jugador y la del CPU.
def eleccion_jugador(op):
    Lista = []
    #Asigna la opción del jugador según la entrada seleccionada.
    if op == 1:
        jugador = PIEDRA
    elif op == 2:
        jugador = PAPEL
    elif op == 3:
        jugador = TIJERA
    else:
        jugador = None
    Lista.append(PIEDRA)
    Lista.append(PAPEL)
    Lista.append(TIJERA)

    opcion_CPU = choice(Lista)
    return jugador,opcion_CPU

#Diccionario que define las reglas del juego.
Piedra_papel_tijera = {(PIEDRA, TIJERA): JUGADOR,
                       (PIEDRA, PAPEL): CPU,
                       (TIJERA, PAPEL): JUGADOR,
                       (TIJERA, PIEDRA): CPU,
                       (PAPEL, PIEDRA): JUGADOR,
                       (PAPEL, TIJERA): CPU,
                       }

while op!= 0: #El juego continúa mientras el jugador no elija salir.
    op = menu() #Muestra el menú y obtiene la opción del jugador.
    jugador,opcion_CPU =eleccion_jugador(op)   #Obtiene la elección del jugador y del CPU.
    #Resultado del juego usando el diccionario.
    Resultado = Piedra_papel_tijera.get((jugador,opcion_CPU), EMPATE)

    if op == 0: #Salir del programa.
        print()
        print("Fin del programa.")

    #Actualiza los contadores y muestra el resultado.
    elif Resultado == JUGADOR:
        Victorias_del_jugador += 1
        print(f"Jugador: {op} CPU: {opcion_CPU} {JUGADOR}")
    elif Resultado == CPU:
        Victorias_del_CPU += 1
        print(f"Jugador: {op} CPU: {opcion_CPU} {CPU}")
    elif Resultado == EMPATE:
        Empates += 1
        print(f"Jugador: {op} CPU: {opcion_CPU} {EMPATE}")
    else:
        print()
        print("Opción incorrecta.")

