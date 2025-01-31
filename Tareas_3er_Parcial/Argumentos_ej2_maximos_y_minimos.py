"""
Este programa realiza la suma de todos los números pares ingresados por el usuario.
Para ello:

a) Solicite al usuario los números enteros. Nota: Hay que validar que tengan el formato adecuado.
b) Utilice una función con argumentos variables que devuelva la suma de los números pares.
c) Muestre el resultado en consola.
"""
def numero_maximo(*vargs) -> tuple:
    maximo = vargs[0]
    for i in vargs:
        if i > maximo:
            maximo = i
    return maximo

def numero_minimo(*vargs) -> tuple:
    minimo = vargs[0]
    if len(vargs) == 0:
        for i in vargs:
            if i > maximo:
                maximo = i
            if i < minimo:
                minimo = i
    return minimo

def cadena_a_flotante(cadena: str) -> float | None:
    # Función que convierte una cadena a un número flotante.
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip('-').replace(".", "")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None


def main() -> None:
    numeros_validos = []  # Tupla que almacena los números válidos que ingrese el usuario.
    contador = 1

    # Bucle que solicitará los números al usuario.
    while True:  # Bucle infinito
        numero = input(f"Ingresa un número {contador}, para terminar ingresa 'fin': ")
        if numero.lower() == 'fin':  # Condición para que al ingresar 'fin', termine el ingreso de números.
            break

        no_puntos = numero.count(".")
        no_guiones = numero.count("-")
        revisar_numero = numero.lstrip('-').replace(".", "")

        if revisar_numero.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
            numeros_validos.append(float(numero))
            contador += 1  # Aumenta el valor del contador cada que el usuario ingresa un número válido.
        else:
            print("Entrada no válida. Por favor ingrese un número válido (entero o decimal).")

    # Validación después de terminar de ingresar los números
    if numeros_validos:
        # Calcula y muestra el número máximo y mínimo.
        maximo = numero_maximo(*numeros_validos)
        minimo = numero_minimo(*numeros_validos)
        print(f"El número máximo es: {maximo}")
        print(f"El número mínimo es: {minimo}")
    else:
        print("No se ingresaron números válidos.")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()