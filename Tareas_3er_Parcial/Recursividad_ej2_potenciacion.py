"""
#rosalinda aquino
# Descripción del programa:
# Este programa calcula la potencia de un número a otro número de manera recursiva. Ambos son números enteros positivos ingresados por el usuario.
# Notar que: a^b = a*(a^(b-1)).
# Para ello:
# a) Solicite al usuario ambos números, validando que tengan el formato adecuado.
# b) Utilice una función recursiva para calcular la potencia, indicando el caso base y el caso recursivo.
# c) Muestre el resultado en consola.
"""
def potencia(base: int , exponente: int )->str | int:
    if base == 0 and exponente == 0:
       return "indeterminado"
    # Caso base.
    if exponente == 0:
        return 1
    else:
        return base * potencia(base,exponente - 1)


def es_numero_valido(cadena: str) -> bool:
    if cadena.isnumeric():
        return True
    else:
        return False

def es_numero_valido2(cadena1: str) -> bool:
    if cadena1.isnumeric():
        return True
    else:
        return False

def main()->None:
    print("********  Programa que imprime los números de manera recursiva.  ********")
    print()

    # Se solicita un número y se valida que sea entre 0 y un entero positivo.
    base = input("Ingresa un número entre 0 y un entero positivo: ")
    exponente = input("Ingresa un número entre 0 y un entero positivo: ")
    print()
    # Si es un número válido, se llama a las funciones recursivas.
    # En caso contrario, finaliza el programa.
    if es_numero_valido(base) and es_numero_valido2(exponente):
        base = int(base)
        exponente = int(exponente)
        resultado = potencia(base, exponente)
        print(f"El resultado es {resultado}")
    else:
        print("Numero no válido, ingrese otro.")

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    main()

