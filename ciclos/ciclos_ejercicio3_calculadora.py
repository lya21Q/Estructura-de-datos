'''
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción:
Cálculadora básica.
'''


op=None
while op != 0  :
    print("calculadora basica")
    print("[1].-Suma: ")
    print("[2].-: Resta ")
    print("[3].-: Multiplicación ")
    print("[4].-: División")
    print("[5].-: División entera")
    print("[6].-: exponenciación")
    print("[0].-: Salir del programa")

    op=int(input("ingrese una opción"))

    if op ==1 :
        numero1=float(input("ingresa un numero: "))
        numero2 =float(input("ingresa segundo numero: "))
        print(numero1 + numero2)
    elif op==2 :
        numero1=float(input("ingresa un numero: "))
        numero2 =(float
                  (input("ingresa segundo numero: ")))
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
    elif op ==0 :
        op=0
        print("salio del programa")
