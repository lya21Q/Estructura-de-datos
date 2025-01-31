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
def potencia(base: int , potencia: int )->str | int:
    if base == 0 and potencia== 0:
       return"indeterminado"
    # Caso base.
    if potencia == 0:
        return 1
    else:
       return base * (base ** (potencia - 1))


def es_numero_valido(cadena: int) -> bool:
    if cadena.isnumeric():
        return True
    else:
        return False

def main()->None:
    print("          ********  Programa que imprime los números de manera recursiva.  ********")
    print()

    # Se solicita un número y se valida que sea entre 0 y un entero positivo.
    base= int(input("Ingresa un número entre 0 y un entero positivo: "))
    potencia = int(input("Ingresa un número entre 0 y un entero positivo: "))
    print()
    # Si es un número válido, se llama a las funciones recursivas.
    # En caso contrario, finaliza el programa.
    if es_numero_valido(base) and es_numero_valido(potencia):
        numero = int(base)
        numero1 = int(potencia)
        resultado=potencia

        print(f"El numero {base} elevado a {potencia} es {resultado}:")
    else:
        print("Numero no válido, ingrese otro.")

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

