
'''
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción: Cálculadora básica.
'''

def menu ():
    op=None
    #Función que muestra el menú al usuario.
    while op != 0  :
        print("calculadora basica")
        print("[1].-Suma: ")
        print("[2].-: Resta ")
        print("[3].-: Multiplicación ")
        print("[4].-: División")
        print("[5].-: División entera")
        print("[6].-: exponenciación")
        print("[0].-: Salir del programa")
        #Solicita al usuario ingresar una opción.
        op=int(input("ingrese una opción:"))
        return op

def calculadora(op,numero1,numero2):
    #Opción para salir del programa.
    if op ==0 :
        print("salio del programa")
    #Opción para realizar una suma.
    elif op ==1 :
        resultado=numero1 + numero2
    # Opción para realizar una resta.
    elif op==2 :
        resultado =numero1 - numero2
    # Opción para realizar una multiplicación.
    elif op==3 :
        resultado=numero1 * numero2
    # Opción para realizar una división.
    elif op==4 :
        resultado=numero1 / numero2
    # Opción para realizar el módulo de 2 números.
    elif op==5 :
        resultado=numero1 % numero2
    # Opción para realizar una división entera.
    elif op == 6 :
        resultado=numero1 // numero2
    else:
        print("Opción no válida.")
    return resultado
#Llamada de la función.
op=menu()
#Solicita al usuario dos números.
numero1 = float(input("ingresa un numero: "))
numero2 = float(input("ingresa segundo numero: "))
#Llamada de la función.
resultado=calculadora(op,numero1,numero2)
print(f"El resultado de la operacòn es: {resultado:.2f}")#Muestra el resultado de la operación.