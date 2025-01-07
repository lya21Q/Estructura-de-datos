#Rosalinda Aquino.
#02 de diciembre del 2024.
#Descripción:
#Este programa es una versión del juego "Piedra, papel o tijeras" que utiliza un diccionario.
#Permite registrar las victorias del jugador, los empates y las victorias del CPU.

"""
Escribe un programa de nombre Diccionarios_ej1_piedra_papel_tijera.py que realice lo siguiente:
Este programa es una nueva versión del juego realizado de piedra, papel y tijeras, pero utilizando un diccionario para las reglas del juego.
El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Se debe mostrar el siguiente menú:
  ***  Juego de piedra, papel o tijeras  ***
1) Piedra.
2) Papel.
3) Tijeras.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Muestre el menú en una función que pida al usuario una de las opciones: piedra, papel o tijeras.
b) Utilice un diccionario para las distintas combinaciones.
c) Realice la lógica adecuada para determinar al ganador. Se requiere que utilice al menos una función.
d) Muestre la elección del jugador y la del cpu.
e) Muestre la cantidad de victorias, empates y derrotas.
f) Repita nuevamente el menú hasta salir.
Observe la salida de la consola como guía:
"""
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
    #CPU elige aleatoriamente entre las opciones.
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
#Ciclo principal del juego.
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
        print("Opción incorrecta.") #Mensaje para opciones no válidas.

