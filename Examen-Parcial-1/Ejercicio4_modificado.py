from random import randint
#Rosalinda Aquino Pérez
#03 Noviembre 2024
#a) El número a adivinar es un número aleatorio entre 1 y 100.
n_adivinar=0
intentos =0
numero=0

var=input("¿En que dificultad deseas jugar: (dificil, facil, medio)?")
var=var.lower()

if var == "dificil" :
    n_adivinar=(1,110)
    intentos = 10
if var == "medio" :
    n_adivinar = (1, 110)
    intentos =5
if var == "facil" :
    intentos = 4



while numero >= intentos:
    numero = int(input("Ingresa un número entre : (1-100): "))
        if numero >= n_adivinar :
            print("El número es mayor")
        elif numero <= n_adivinar :
            print("El numero a adivinar es mayor")
        else :
            print(f"¡Felicidades! adivinate el número en : {intentos} intentos ")
            break
    if numero!= n_adivinar :
        print(f"lo sentimos el numero a adivinar era : {n_adivinar}")

#e) Si el jugador no adivina el número, el juego muestra un mensaje con el número.

#solicitar inicialmente la dificultad
#f 10intentos y números 1-50
#m lo que tiene
#D 4 intentos numeros entre el 1-110