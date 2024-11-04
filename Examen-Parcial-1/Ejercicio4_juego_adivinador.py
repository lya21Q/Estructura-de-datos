from random import randint
#Rosalinda Aquino Pérez
#03 Noviembre 2024
#a) El número a adivinar es un número aleatorio entre 1 y 100.
n_adivinar = randint(1,100)
intentos =1

#b) El jugador tendrá 5 intentos para encontrar el número.
while intentos <= 5:
    print(f"Numero de intento: {intentos}.",end=" ")#Se va imprimiendo el número de intentos seguido de un mensaje para ingresas posteriormente un número, esto con ayuda de el comando end= " ".
    numero = int(input("Ingresa un número entre : (1-100): "))

    if numero < n_adivinar :
        print("El numero a adivinar es mayor")#c) Como pista, el juego indicará si el número a adivinar es menor o mayor al número ingresado, si el número no es el correcto.
    elif numero > n_adivinar:
        print("El número a adivinar es menor")
    else :
        # d) Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.
        print(f"¡Felicidades! adivinate el número en : {intentos} intentos ")
        break
    intentos += 1

#e) Si el jugador no adivina el número, el juego muestra un mensaje con el número.
if numero != n_adivinar :
    print(f"Perdiste el número a adivinar era : {n_adivinar}")


