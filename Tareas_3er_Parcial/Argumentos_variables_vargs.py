"""
Nombre: Alberto Martínez Barbosa.
Fecha:
Descripción:
En Python, *args es una sintaxis especial que permite a una función aceptar un número variable de
argumentos posicionales. Es decir, puedes pasar a la función tantos argumentos como quieras,
y estos se empaquetarán en una tupla dentro de la función.

Consideraciones importantes:
- Orden: Los argumentos regulares deben ir antes de *args.
- Nombre: Aunque se suele usar args, puedes usar cualquier otro nombre, pero es una convención usar args.
- Tupla: Los argumentos capturados por *args siempre se empaquetan en una tupla.
- Mandar listas como *vargs: Al llamar una función debe ser de la forma *lista, ya que el operador * desempaqueta
         los elementos de la lista y los manda como argumentos individuales.
"""

def calcular_promedio(materia: str = None, *vargs) -> None:
    """
    Función que muestra el promedio de una materia con argumentos variables.
    :param materia: Nombre de la materia.
    :param vargs: Calificaciones del usuario.
    """

    # Se calcula el promedio (si hay argumentos) y se muestra en la consola.
    promedio = None
    if len(vargs) != 0:
        promedio = sum(vargs)/len(vargs)

    print(f"El promedio de la materia {materia} es: {promedio:.2f}")



def cadena_a_flotante(cadena: str) -> float | None:
    """
    Función que convierte una cadena a un número flotante.
    :param cadena: Cadena a convertir.
    :return: Regresa el número flotante si cumple con el formato, en caso contrario, devuelve None.
    """

    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-').replace(".","")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None



def main() -> None:
    """
    Función principal.
    """

    print("          ********  Programa que calcula el promedio de las calificaciones.  ********")
    print()

    # Prueba del llamado a la función con argumentos variables.
    print("Prueba del llamado a la función con argumentos variables.")
    calcular_promedio("Prueba", 8.5, 8.5, 9)
    print()


    # Prueba con datos del usuario.
    print("Prueba del llamado a la función con argumentos variables ingresados por la consola.")
    materia = input("Ingresa el nombre de la materia: ")

    # Se solicitan las calificaciones mediante un ciclo, el cual termina hasta ingresar 'enter'.
    # Las calificaciones se almacenan en una lista.
    calificaciones = []
    num_cadena = input(f"Ingresa la calificación [{len(calificaciones) + 1}] o presiona enter para continuar: ")

    while bool(num_cadena):
        numero = cadena_a_flotante(cadena= num_cadena)

        if numero is None:
            print("Formato no válido, intenta nuevamente.")

        else:
            calificaciones.append(numero)

        num_cadena = input(f"Ingresa la calificación [{len(calificaciones) + 1}] o presiona enter para continuar: ")

    # Una vez ingresadas todas las calificaciones, se calcula e imprime el promedio.
    # IMPORTANTE:
    # Es este caso, calificaciones es una lista, por lo que el operador * desempaqueta los elementos de la lista
    # y los manda como argumentos individuales.
    calcular_promedio(materia, *calificaciones)



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()