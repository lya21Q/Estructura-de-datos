"""Calculadora básica"""

#1)Suma
#2)resta
#3)multiplicación
#4)División
#5)Division entera
#6)Exponenciación
#7)ingresa un menú


op=1

while op != 7  :
    print("calculadora basica")
    print("[1].-Suma: ")
    print("[2].-: Resta ")
    print("[3].-: Multiplicación ")
    print("[4].-: División")
    print("[5].-: División entera")
    print("[6].-: exponenciación")
    print("[7].-: Salir del programa")

    op:int(input("ingrese una opción"))

    if op ==1 :
        numero1=int(input("ingresa un numero: "))
        numero2 = int(input("ingresa segundo numero: "))
        print(numero1 + numero2)
    elif op==2 :
        numero1=int(input("ingresa un numero: "))
        numero2 = int(input("ingresa segundo numero: "))
        print(numero1 - numero2)
    elif op==3 :
        numero1=int(input("ingresa un numero: "))
        numero2 = int(input("ingresa segundo numero: "))
        print(numero1 * numero2)
    elif op==4 :
        numero1=int(input("ingresa un numero: "))
        numero2 = int(input("ingresa segundo numero: "))
        print(numero1 / numero2)
    elif op==5 :
        numero1=int(input("ingresa un numero: "))
        numero2 = int(input("ingresa segundo numero: "))
        print(numero1 % numero2)
    elif op == 6 :
        numero1=int(input("ingresa un numero: "))
        numero2 = int(input("ingresa segundo numero: "))
        print(numero1 // numero2)
    elif op ==7 :
        print("Saliendo del programa")

if op != 7 :
    print("")
else :