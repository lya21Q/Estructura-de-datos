


def cadena_a_entero(cadena:str):#especificar el tipo de dato que s eva a enviar.
    no_guiones=cadena.cout("-")
    revisar_cadena=cadena.lstriṕ("-")
        if revisar_cadena.isNumeric():
            and no_guiones in (0,1)
            return int(cadena)
        else:
            return None






if opcion==2:
    num_cadena=input("ingresa el numero a convertir")
    numero=cadena_a_numero(num_cadena)
    while  numero is None:
        num_cadena=input("Opción no válida, intente de nuevo.")
        numero=cadena_a_entero(num_cadena)
        print(f"{numero} es de tipo {type(numero)}")