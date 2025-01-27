def menu() -> int:
    """
    Función que muestra el menú del programa.
    :return: Regresa el número cero o un entero positivo.
    """

    print("  ***  Conversión a números enteros y flotantes con verificación ***")
    print("     1) Convertir a entero.")
    print("     2) Convertir a flotante.")
    print("     0) Salir.")
    print()

    opcion = input("Ingresa una de las opciones: ").strip()

    while not opcion.isnumeric():
        opcion = input("Opción no válida, intenta nuevamente: ")

    print()

    return int(opcion)


def cadena_a_entero(cadena: str) -> int | None:
    """
    Función que convierte una cadena a un número entero.
    :param cadena: Cadena a convertir.
    :return: Regresa el número entero si cumple con el formato, en caso contrario, devuelve None.
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip('-')

    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None


def cadena_a_flotante(cadena: str) -> float | None:
    """
    Función que convierte una cadena a un número flotante.
    :param cadena: Cadena a convertir.
    :return: Regresa el número flotante si cumple con el formato, en caso contrario, devuelve None.
    """

    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip('-').replace(".", "")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None


# Ahora se tiene la función main(). Tod0 lo que estaba en el código a nivel de módulo, ahora se coloca
# en esta función.
def main() -> None:
    """
    Función principal.
    """

    # Ciclo que contiene el menú.
    opcion = None

    while opcion != 0:

        opcion = menu()

        # Se escoge convertir a un número entero.
        if opcion == 1:
            num_cadena = input("Ingresa el número a convertir: ")
            numero = cadena_a_entero(num_cadena)

            while numero is None:
                num_cadena = input("Formato no válido, intenta nuevamente: ")
                numero = cadena_a_entero(num_cadena)

            print()
            print(f"El número {numero} es de tipo {type(numero)}.")

        # Se escoge convertir a un número flotante.
        elif opcion == 2:
            num_cadena = input("Ingresa el número a convertir: ")
            numero = (cadena_a_flotante(num_cadena))

            while numero is None:
                num_cadena = input("Formato no válido, intenta nuevamente: ")
                numero = cadena_a_flotante(num_cadena)

            print()
            print(f"El número {numero} es de tipo {type(numero)}.")

        # Se escoge salir del programa.
        elif opcion == 0:
            print("Fin del programa.")

        # Se escoge una opción no válida.
        else:
            print("Opción no válida.")

        print("------------------------------------------------------------------")
        print()


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
# Ahora, en el código a nivel de módulo, únicamente se revisa que este script se esté ejecutando directamente.
# Si es el caso, entonces llama a la función principal.
if __name__ == '__main__':
    main()