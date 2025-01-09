opcion=None

def menu()->int:
    """
    :return: {Muestra el menú del programa, devuelve el entero que haya elegido el usuario.}
    """
    print("[1].-Cadena a entero.")
    print("[2].-Cadena a flotante.")
    print("[0].-Salir")
    opcion=int(input("Ingrese una opción:"))
    return opcion

def cadena_a_entero(cadena:str)->int|None:#especificar el tipo de dato que se va a enviar.
    """
    :param cadena:Es la cadena a convertir a número entero. Función que convierte una cadena a número entero con validación.
    :return:Devuelve el número entrero, en caso de no tener el formato de validación devuelve None.
    """
    no_guiones=cadena.count("-")
    revisar_cadena=cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1) :
        return int(cadena)
    else:
        return None

def cadena_a_flotante(cadena:str)->float|None:
    no_guiones=cadena.count("-")
    no_puntos=cadena.count(".")
    revisar_cadena=cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in (0,1) and no_puntos in (0,1):
        return float(cadena)
    else:
        return None

while opcion!=0:
    opcion = menu()
    if opcion==1:
        num_cadena:str=input("ingresa el numero a convertir:")
        numero=cadena_a_entero(num_cadena)
        while numero is None:
            num_cadena=input("Opción no válida, intente de nuevo:")
            numero=cadena_a_entero(num_cadena)
        print(f"{numero} es de tipo {type(numero)}")
    elif opcion ==2:
        num_cadena:str=input("Ingresa el número a convertir:")
        numero=cadena_a_flotante(num_cadena)
        while numero is None:
            num_cadena=input("Opción no válida, intente de nuevo:")
            numero=cadena_a_flotante(num_cadena)
        print(f"{numero} es de tipo {type(numero)}")
    elif opcion==0:
            print("Saliendo...")
    else:
        print("Opción no válida.")