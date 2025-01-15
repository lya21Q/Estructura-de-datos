opcion=None
def menu()->int:
    print("***Menu**")
    print("[1].- Sumar")
    print("[2].- Restar")
    print("[3].-Salir")
    opcion = int(input("Ingrese una opcion:"))
    return opcion

def suma(resultado:str)->float|None:
    no_guiones=resultado.count("-")
    no_puntos=resultado.count(".")
    revisar_resultado=resultado.lstrip("-").replace(".","")
    if revisar_resultado.isnumeric() and no_guiones in (0,1) and no_puntos in (0,1):
        return float(resultado)
    else:
        return None

def resta(resultado:str)->float|None:
    no_guiones=resultado.count("-")
    no_puntos=resultado.count(".")
    revisar_resultado=resultado.lstrip("-").replace(".","")
    if revisar_resultado.isnumeric() and no_guiones in (0,1) and no_puntos in (0,1):
        return float(resultado)
    else:
        return None

def main()->None:
    while opcion !=3:
        opcion = menu()
        if opcion == 1:
            num1 = float(input("Ingrese un numero:"))
            resultado = num1 + num2
            resultado = suma(num1, num2)
        elif opcion == 2:
            num2 = float(input("Ingrese un segundo número:"))
            resultado = num1 - num2
            resultado = resta(num1, num2)
        else:
            print("Opción no válida")

if __name__=="main":
    print(__name__)
    main()