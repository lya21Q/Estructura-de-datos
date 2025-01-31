"""
Este programa realiza la suma de todos los números pares ingresados por el usuario.
Para ello:

a) Solicite al usuario los números enteros. Nota: Hay que validar que tengan el formato adecuado.
b) Utilice una función con argumentos variables que devuelva la suma de los números pares.
c) Muestre el resultado en consola.
"""

def numeros_pares(*vargs) -> int:# Función que verifica si los números son pares y devuelve la suma de ellos.
    suma_pares = 0
    for numero in vargs:
        if numero % 2 == 0:  # Comprueba si el número es par.
            suma_pares += numero
            print(f"El {numero} es par.")
    return suma_pares

def cadena_a_flotante(cadena: str) -> float | None:# Función que convierte una cadena a un número flotante.
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip('-').replace(".", "")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None

def main() -> None:
    numeros_validos = []#Tupla que almacena los numeros, validos que ingrese el usuario.
    contador = 1

    # Bucle que solicitará los números al usuario.
    while True:#Bucle infinito
        numero = input(f"Ingresa un número {contador}, para terminar ingresa 'fin': ")
        if numero.lower() == 'fin':#Condicio para que al ingresar fin, termine el ingreso de numeros.
            break

        no_puntos = numero.count(".")
        no_guiones = numero.count("-")
        revisar_numero = numero.lstrip('-').replace(".", "")

        if revisar_numero.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
            numeros_validos.append(float(numero))
            contador += 1 #Aumenta el valor del contador cada que el usuario ingresa un número válido.
        else:
            print("Entrada no válida. Por favor ingrese un número válido (entero o decimal).")

    # Validación después de terminar de ingresar los números
    if numeros_validos:
        # Calcula y muestra la suma de los números pares.
        suma_pares = numeros_pares(*numeros_validos)
        print(f"La suma de los números pares es: {suma_pares}")
    else:
        print("No se ingresaron números válidos.")

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
