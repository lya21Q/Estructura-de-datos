opcion=None
def menu()->int:
    print("***Menú**")
    print("[1].- Sumar")
    print("[2].- Restar")
    print("[3].- Multiplicaccion")
    print("[0].-Salir")
    opcion = int(input("Ingrese una opcion:"))
    return opcion

def cadena_a_flotante(cadena:str)->float|None:
    no_guiones=cadena.count("-")
    no_puntos=cadena.count(".")
    revisar_cadena=cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in (0,1) and no_puntos in (0,1):
        return float(cadena)
    else:
        return None

def suma(num1,num2):
    resultado=num1+num2
    return resultado

def resta(num1,num2):
    resultado=num1-num2
    return resultado

def multiplicacion(num1,num2):
    resultado=num1*num2
    return resultado

def main()->None:
    opcion=None
    while opcion!=0:
        opcion=menu()
        if opcion==0:
            print("Saliendo del programa.")
        elif opcion==1:
            numero1:str=input("Ingrese un número:")
            numero2:str=input("Ingrese un segundo número:")
            num1=cadena_a_flotante(numero1)
            num2=cadena_a_flotante(numero2)
            while num1 and num2 is None:
                numero1:str=input("Opción no válida, intente de nuevo:")
                numero2:str=input("Opción no válida, intente de nuevo:")
            resultado=suma(num1,num2)
            print(f"la suma es {resultado}")
        elif opcion==2:
            numero1:str=input("Ingrese un número:")
            numero2:str=input("Ingrese un segundo número:")
            num1=cadena_a_flotante(numero1)
            num2=cadena_a_flotante(numero2)
            while num1  and num2 is None:
                numero1:str=input("Opción no válida, intente de nuevo:")
                numero2:str=input("Opción no válida, intente de nuevo:")
            resultado=resta(num1,num2)
            print(f"la suma es {resultado}")
        elif opcion==3:
            numero1:str=input("Ingrese un número:")
            numero2:str=input("Ingrese un segundo número:")
            num1=cadena_a_flotante(numero1)
            num2=cadena_a_flotante(numero2)
            while num1  and num2 is None:
                numero1:str=input("Opción no válida, intente de nuevo:")
                numero2:str=input("Opción no válida, intente de nuevo:")
            resultado=multiplicacion(num1,num2)
            print(f"la suma es {resultado}")
        else:
            print("Saliendo del programa.")

if __name__=="__main__":
    main()