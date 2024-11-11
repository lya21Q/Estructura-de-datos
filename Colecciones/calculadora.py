#reciba tres numeron
def menu(op) :
    while op != 7:
        num1 = int(input("Ingrse u número :"))
        num2 = int(input("Ingrse u número :"))
        print("calculadora basica")
        print("[1].-Suma: ")
        print("[2].-: Resta ")
        print("[3].-: Multiplicación ")
        print("[4].-: División")
        print("[5].-: División entera")
        print("[6].-: exponenciación")
        print("[7].-: Salir del programa")
    op = int(input("ingrese una opción"))
    return menu
#suma
#resta+
#multiplicación
#divión
#potencia
def calculadora(opcion, num1, num2):
    num1=num1+num2
    print(num1+num2)
    num1=num1-num2
    print(num1 * num2)
    num1=num1*num2
    print(num1 / num2)
    num1=num1/num2
    print(num1 / num2)
    num1=num1/num2
    print(num1 / num2)
    num1=num1**num2
    return calculadora
