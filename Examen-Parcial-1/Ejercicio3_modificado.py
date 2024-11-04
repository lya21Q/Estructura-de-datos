#Rosalinda Aquino Pérez
#03 Noviembre 2024
from random import randint, Random
op=0
empates=0
victorias=0
victorias_jugador=0
print("*** Juego de piedra, papel o tijera ***")
print(f"Victorias del jugador : {victorias}, empates :{empates}, victorias del CPU : {victorias_jugador}")
op=input("ingrese opción: (piedra,papel,tijera:) ")
CPU=("piedra","papel""tijera")
while op!= CPU :
    if op =="piedra" and CPU =="piedra"  or op == "papel" and CPU=="papel" or op=="tijera" and CPU=="tijera" :
        print("Hubo un empate")
        empates+=1
        print()
    elif op == "piedra" and CPU=="papel" :
        print("El ganador es CPU")
        print()
    elif op == "papel" and CPU== "piedra" :
        victorias += 1
        print("El ganador es CPU")
        print()
    elif op == "tijera" and CPU == "papel":
        victorias += 1
        print("El ganador es CPU")
        print()
    elif CPU == "piedra" and op == "papel" :
        victorias_jugador +=1
        print("El ganador es jugador")
        print()
    elif CPU == "papel" and op == "tijera" :
        victorias_jugador +=1
        print("El ganador es jugador ")
        print()
    elif CPU == "tijera" and op == "papel":
        victorias_jugador +=1
        print("El ganador es jugador ")
        print()
    else :
        print("opcion no válida")
        break