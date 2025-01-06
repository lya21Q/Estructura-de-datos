'''
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción:Este programa es una lista de las calificaciones de los alumnos del Parcial 1. La lista está conformada por el nombre del alumno y sus calificaciones.
Cada alumno tiene 5 calificaciones: estructuras de datos, derecho, contabilidad, álgebra y electrónica.
Se debe mostrar el siguiente menú:
  *** Calificaciones del Parcial 1 ***
1) Ver calificaciones de todos los alumnos.
2) Ver calificaciones detalladas de un alumno.
3) Ver promedios del Parcial 1 de todos los alumnos.
4) Ver promedio grupal del Parcial 1.
5) Agregar alumno y sus calificaciones.
6) Eliminar alumno y sus calificaciones.
0) Salir.
Cualquier otro caso -> Opción no válida.
'''
op=None
def menu():
    print("[1].-Ver calificaciones de todos los alumnos.")
    print("[2].-Ver calificaciones detalladas de un alumno.")
    print("[3].-Ver promedios del Parcial 1 de todos los alumnos.")
    print("[4].- Ver promedio grupal del Parcial 1.")
    print("[5].-Agregar alumno y sus calificaciones.")
    print("[6].-Eliminar alumno y sus calificaciones.")
    print("[0].- Salir.")
    op=int(input("Ingrese una opción:"))
    return op

alumnos=[]
estructura_de_datos=[]
derecho=[]
contabilidad=[]
algebra=[]
electronica=[]
calificacion=None
while op!=0:
    op = menu()
    #Caso para salir del programa.
    if op==0:
        print("Saliendo del programa...")
    #Caso para ver calificaciones de todos los alumnos.
    elif op==1:
        print("Las calificaciones de todos los alumnos son:")
        for alumno in range (len(alumnos)):
            print(f"El alumno:{alumnos}, calificaciones: {estructura_de_datos},{derecho},{contabilidad},{algebra},{electronica}")
    #Caso para ver calificaciones detalladas de un alumno.
    elif op==2:
        alumno_1=input("Ingresa el nombre del alumno:")
        for alumno in alumnos:
            if alumno_1==alumnos:
                print(f"Calificaciones del alumno:{alumno_1}{estructura_de_datos}{derecho}{contabilidad}{algebra}{electronica}")
    #Caso para ver promedios del parcial 1 de todos los alumnos.
    elif op==3:
        print()
    #Caso para ver promedio grupal del parcial 1.
    elif op==4:
        if len(alumnos)>0:
            total_promedio=sum(estructura_de_datos+derecho+contabilidad+algebra+electronica)
            print(f"Promedio grupal del parcial 1 es: {total_promedio}")
    #Caso pra agregar alumno y sus calificaciones.
    elif op==5:
        alumno=input("Ingrese el nombre del alumno:")
        cal_estructura=float(input("Ingresa la calificacion de estructura de datos: "))
        cal_derecho = float(input("Ingresa la calificacion de derecho: "))
        cal_contabilidad = float(input("Ingresa la calificacion de contabiliidad: "))
        cal_algebra = float(input("Ingresa la calificacion de algebrà: "))
        cal_electronica = float(input("Ingresa la calificacion de electronica: "))

        alumnos.append(alumno)
        estructura_de_datos.append(cal_estructura)
        derecho.append(cal_derecho)
        contabilidad.append(cal_contabilidad)
        algebra.append(cal_algebra)
        electronica.append(cal_electronica)
    #Caso para eliminar alumno y sus calificaciones.
    elif op==6:
        print()

op=menu()
