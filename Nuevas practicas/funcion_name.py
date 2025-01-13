
opcion=None
def menu():
    print("***Menu**")
    print("[1].- Sumar")
    print("[2].- Restar")
    print("[0].-Salir")
    opcion=input("Ingrese una opcion:")
    return opcion


def suma(numeros:str)->float|None:
    no_guiones=numeros.count("-")
    no_puntos=numeros.count(".")
    revisar_cadena=numeros.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in (0,1) and no_puntos in (0,1):
        return float(numeros)
    else:
        return None

def resta(numeros:str)->float|None:
    no_guiones=numeros.count("-")
    no_puntos=numeros.count(".")
    revisar_cadena=numeros.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in (0,1) and no_puntos in (0,1):
        return float(resultado)
    else:
        return None

while opcion!=0:
    opcion=menu()
    if opcion==1 :
        num1=input("Ingrese un numero:")
        resultado=num1+num2
        resultado=suma(num1,num2)
    elif opcion==2 :
        num2=input("Ingrese un segundo número:")
        resultado = num1 - num2
        resultado=resta(num1,num2)
    else:
        print("Opción no válida")

