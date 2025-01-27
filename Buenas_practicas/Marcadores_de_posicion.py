"""
Nombre: Alberto Martínez Barbosa.
Fecha:
Descripción:
En este archivo se muestra el uso de los marcadores de posición.
Cuando se diseña un programa y aún no se implementa cierta parte del código, se pueden utilizar
los marcadores de posición para evitar errores de sintaxis y mantener la estructura del programa.
Esto permite trabajar en otras secciones sin desarrollar la implementación de esa parte específica.

Marcadores:
- pass
- 3 puntos: ...
- Generar un error.

TODO y FIXME son herramientas muy útiles para marcar estos puntos en el código.

TODO: Indica una tarea que aún debe completarse. Es como una lista de pendientes dentro del código.
FIXME: Señala un problema conocido que necesita ser arreglado.
       Es una especie de etiqueta para indicar un bug o una parte del código que no funciona como debería.

Para ver:
- View - Tool windows - TODO
"""

""" %%%%%%%     FUNCIONES    %%%%%%%%%%%%%%%%%%%%% """
# TODO realizar la función del menú.
def menu():
    pass

# FIXME Realizar la función.
def cadena_a_entero(cadena):
        ...

# TODO Realizar la conversión de cadena a flotante.
def cadena_a_flotante(cadena: str) -> float | None:
    raise NotImplementedError("Falta por desarrollar esta función.")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
# Ciclo que contiene el menú.
opcion = None

while opcion != 0:

    # Como prueba, se utiliza una variable 2, ya que aún no se ha implementado la función menu()
    #opcion = menu()
    opcion = 2

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