alumnos={'nombre':"Rosalinda",'Electronica':0,'Algebra':0,'Estructura de datos':0,'Derecho y legislacion':0,'Contabilidad':0,'Ingles':0}

def menu()->int:
    """
    Función que muestra el menú de opciones para realizar
    :return: Retorna la opción seleccionada por el usuario
    """
    print("Promedio de un alumno")
    print("1) Calcular promedio de un alumno")
    print("0) Salir")
    opcion = (input("Teclea la opción que desea realizar: "))
    while not opcion.isnumeric():
        print("opción no válida")
        opcion = input("ingrese número nuevamente: ")
    opcion = int(opcion)
    return opcion


def cadena_a_flotante (cadena):
    """
    Función que transforma una cadena a número flotante
    :param cadena: Cadena introducida por el usuario
    :return: Número flotante o en dado caso nada
    """
    no_puntos=cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_puntos in (0,1) and no_guiones in (0,1):
        return float(cadena)
    else:
        return None

def ingresar_alumno(alumnos):
    """
    Función para insertar un alumno con todas y sus calificaciones correspondientes y obtener el promedio del alumno
    :param alumnos: diccionario donde se introducen los valores
    :return:
    """
    alumno=input("Ingrese nombre del alumno: ")
    while alumno.isnumeric():
        print("opción no válida")
        alumno = input("Ingrese nuevamente el nombre del alumno: ")
    alumno= str(alumno)
    alumnos['nombre'] =alumno

    electronica= input("Ingrese calificación de la materia de electrónica: ")
    numero = cadena_a_flotante(electronica)
    while numero is None:
        electronica = input("Acción invalida, ingrese nuevamente la calificación de la materia de electrónica: ")
        numero = cadena_a_flotante(electronica)
    alumnos['Electronica'] = electronica

    algebra= input("Ingrese calificación de la materia de Algebra: ")
    numero = cadena_a_flotante(algebra)
    while numero is None:
        algebra = input("Acción inválida, ingrese nuevamente la calificación de la materia de Algebra: ")
        numero = cadena_a_flotante(algebra)
    alumnos['Algebra'] = algebra

    estructura= input("Ingrese calificación de la materia de Estructura de datos: ")
    numero = cadena_a_flotante(estructura)
    while numero is None:
        estructura = input("Acción inválida, ingrese nuevamente la calificación de la materia de Estructura de datos: ")
        numero = cadena_a_flotante(estructura)
    alumnos['Estructura de datos'] = estructura

    derecho= input("Ingrese calificación de la materia de Derecho: ")
    numero = cadena_a_flotante(derecho)
    while numero is None:
        derecho = input("Acción inválida, ingrese nuevamente la calificación de la materia de Derecho: ")
        numero = cadena_a_flotante(derecho)
    alumnos['Derecho y legislacion'] = derecho

    contabilidad= input("Ingrese calificación de la materia de Contabilidad: ")
    numero = cadena_a_flotante(contabilidad)
    while numero is None:
        contabilidad = input("Acción inválida, ingrese nuevamente la calificación de la materia de Contabilidad: ")
        numero = cadena_a_flotante(contabilidad)
    alumnos['Contabilidad'] = contabilidad

    ingles= input("Ingrese calificación de la materia de Ingles: ")
    numero = cadena_a_flotante(ingles)
    while numero is None:
        ingles = input("Acción inválida, ingrese nuevamente la calificación de la materia de Contabilidad: ")
        numero = cadena_a_flotante(ingles)
    alumnos['Ingles'] = ingles

if __name__ == '__main__':
    op=1
    while op!=0:
        opcion = menu()
        if opcion==1:
            ingresar_alumno(alumnos)
            print()
            print("Informacion del alumno:")
            print(alumnos, end=" ")
        elif opcion == 0:
            opcion = 0
            print("Salió del programa")
            break
        else:
            print("opcion incorrecta")