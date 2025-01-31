"""
#Rosalinda Aquino
Instrucciones:

Escribe un programa de nombre Recursividad_ej1_factorial.py que realice lo que se indica en la descripción del programa.

Descripción del programa:
Este programa calcula el factorial de un número entero positivo ingresado por el usuario, utilizando recursividad.

Notar que: n! = n*(n-1)!
Para ello:
a) Solicite al usuario el número al que se requiere calcular el factorial, validando que tenga el formato adecuado.
b) Utilice una función recursiva para calcular el factorial, indicando el caso base y el caso recursivo.
c) Muestre el resultado en consola.
"""

def funcion_recursiva_ascendente(numero: int) -> None:
    if numero == 0:
        print(numero, end= ' ')
    # Caso recursivo. Busca imprimir un número menor antes de imprimir el número requerido.
    else:
        funcion_recursiva_ascendente(numero - 1)
        print(numero, end= ' ')
def funcion_recursiva_descendente(numero: int) -> None:
    if numero == 0:
        print(numero, end= ' ')

    # Caso recursivo. Imprime el número y luego busca imprimir un número menor.
    else:
        print(numero, end= ' ')
        funcion_recursiva_descendente(numero - 1)

def es_numero_valido(cadena: str) -> bool:

    if cadena.isnumeric():
        return True

    else:
        return False

def main() -> None:
    """
    Función principal.
    """

    print("          ********  Programa que imprime los números de manera recursiva.  ********")
    print()

    # Se solicita un número y se valida que sea entre 0 y un entero positivo.
    num_cadena = input("Ingresa un número entre 0 y un entero positivo: ")
    print()

    # Si es un número válido, se llama a las funciones recursivas.
    # En caso contrario, finaliza el programa.
    if es_numero_valido(num_cadena):
        numero = int(num_cadena)

        print(f"Número del 0 al {numero} de manera ascendente:")
        funcion_recursiva_potenciacion(numero)



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
