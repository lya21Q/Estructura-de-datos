#reciba tres numero

def menu() :
        print("calculadora basica")
        print("[1].-Suma ")
        print("[2].-: Resta ")
        print("[3].-: Multiplicación ")
        print("[4].-: División")
        print("[5].-: División entera")
        print("[6].-: exponenciación")
        print("[7].-: módulo")
        print("[8].-: Salir del programa")
        op = int(input("ingrese una opción:"))
        return op

def calculadora(op, num1, num2):
    if op ==1 :
        resultado=num1 + num2
    elif op==2 :
        resultado=num1 - num2
    elif op==3 :
        num1 * num2
    elif op==4 :
        resultado=num1 / num2
    elif op==5 :
        resultado=num1 // num2
    elif op == 6 :
        resultado=num1 ** num2
    elif op == 7:
        resultado = num1 % num2
    elif op==8:
        print("salio del programa")
    else :
        print("Opción no válida")
    return resultado

num1 = float(input("Ingrese un número:"))
num2 = float(input("Ingrese un número:"))
op=menu()
resultado=calculadora(op,num1,num2)
print(f"El resultado es {resultado:.2f}")