def menu() -> int:
    """
    Muestra el menú del programa
    :return: La selección del usuario
    """
    print("[1].- Convertir cadena a entero")
    print("-[2].- Convertir cadena a flotante")
    print("[0].- Salir")
    opcion = int(input("Elige una opción: "))

def cadena_a_entero(cadena: str) -> int | None:  # devolver
    # recibir
    """
    Convierte de cadena a entero validando que tenga el formato adecuado
    :param cadena: Es la cadena a convertir a número entero
    :return: Devuelve un entero
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None


def cadena_a_flotante(cadena: str) -> float | None:  # devolver
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".", "")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None


opcion = None

while opcion != 0:
    opcion = menu()
    if opcion == 1:
        num_cadena: str = input("Ingresa el número a convertir: ")
        num = cadena_a_entero(num_cadena)
        while num is None:
            print("Opción inválida. Ingresa un número entero válido.")
            num_cadena = input("Ingresa el número a convertir: ")
            num = cadena_a_entero(num_cadena)
            print()
        print(f"El número {num} es de tipo {type(num)}")
        print()}
    elif opcion == 2:
        num_cadena: str = input("Ingresa el número a convertir: ")
        num = cadena_a_flotante(num_cadena)
        while num is None:
            print("Opción inválida. Ingresa un número flotante válido.")
            num_cadena = input("Ingresa el número a convertir: ")
            num = cadena_a_flotante(num_cadena)
            print()
        print(f"El número {num} es de tipo {type(num)}")
        print()
    elif opcion==0:
        print()
    else:
        print()