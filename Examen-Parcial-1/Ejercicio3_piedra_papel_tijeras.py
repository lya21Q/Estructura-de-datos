#Rosalinda Aquino Pérez
#03 Noviembre 2024
import random
from random import randint

#Este programa es el famoso juego de "piedra, papel o tijera", en donde el contrincante es la CPU. La opción de la CPU se escogerá de forma aleatorio con la función randint().

#a) Muestre la cantidad de victorias, empates y derrotas.
op=0
empates=0
victorias=0
victorias_cpu=0
while op != 4  :
    # El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Además, mostrará el siguiente menú:
    print("*** Juego de piedra, papel o tijera ***")
    print(f"Victorias del jugador : {victorias}, empates :{empates}, victorias del CPU : {victorias_cpu}")
    print("[1].-Piedra: ")
    print("[2].-: Papel")
    print("[3].-: Tijera ")
    print("[0].-: Salir")

    CPU = randint(1, 3)  # Asignandole a cpu las opciones, piedra, papel o tijera.
# b) Pida al usuario una opción del menú.
    op=int(input("ingrese una opción: "))

    if op ==  CPU :
        print(f"jugador:{op},CPU: {CPU}")
        empates+=1
        print(f"Jugador : {op}. CPU : {CPU}. Empate")
        print()
    elif op == 1 and CPU== 3 :
        print(f"Jugador : {op}. CPU : {CPU}. El gandaor es jugador")
        print()
    elif op == 2 and CPU== 1  :
        victorias += 1
        print(f"Jugador : {op}. CPU : {CPU}. El gandaor es jugador")
        print()
    elif op == 3 and CPU== 2  :
        victorias += 1
        print(f"Jugador : {op}. CPU : {CPU}. El gandaor es jugador")
        print()
    elif CPU == 1 and op == 2  :
        victorias_cpu += 1
        print(f"Jugador : {op}. CPU : {CPU}. El gandaor es CPU")
        print()
    elif CPU == 2 and op == 1  :
        victorias_cpu += 1
        print(f"Jugador : {op}. CPU : {CPU}. El gandaor es CPU")
        print()
    elif CPU == 3 and op == 2  :
        victorias_cpu += 1
        print(f"Jugador : {op}. CPU : {CPU}. El gandaor es CPU")
        print()
    elif op ==0:
        print("Fin del juego")
        break #Finalizar el programa.
    else :
        print("Opción inválida")
        op=0



