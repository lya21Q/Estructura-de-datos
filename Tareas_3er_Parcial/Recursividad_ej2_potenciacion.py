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
def potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def es_numero_valido(cadena: str) -> bool:
    if cadena.isnumeric():
        return True
    else:
        return False

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()

