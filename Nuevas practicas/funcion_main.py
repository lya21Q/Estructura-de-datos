opcion=None
def menu()->int:
    print("***Menú**")
    print("[1].- Sumar")
    print("[2].- Restar")
    print("[0].-Salir")
    opcion = int(input("Ingrese una opcion:"))
    return opcion

def verificar_cadena(resultado:str)->float|None:
    no_guiones=resultado.count("-")
    no_puntos=resultado.count(".")
    revisar_resultado=resultado.lstrip("-").replace(".","")
    if revisar_resultado.isnumeric() and no_guiones in (0,1) and no_puntos in (0,1):
        return float(resultado)
    else:
        return None

def suma(num1,num2):
    resultado=num1+num2
    return resultado

def resta(num1,num2):
    resultado=num1-num2
    return resultado

def main()->None:
    opcion=None
    while opcion!=0:
        opcion=menu()
        if opcion==0:
            print("Saliendo del programa.")
        elif opcion==1:
            num1 = float(input("Ingrese un número:"))
            num2 = float(input("Ingrese un segundo número:"))
            resultado=suma(num1,num2)
            verificar_cadena(resultado)
            print(f"El resultado de la suma es:{resultado}")
        elif opcion==2:
            num1 = float(input("Ingrese un número:"))
            num2 = float(input("Ingrese un segundo número:"))
            resultado=suma(num1,num2)
            verificar_cadena(resultado)
            print(f"El resultado de la suma es:{resultado}")
        else:
            print("Saliendo del programa.")

if __name__=="__main__":
    main()