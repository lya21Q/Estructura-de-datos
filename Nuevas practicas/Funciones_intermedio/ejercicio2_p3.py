"""
Rosalinda Aquino Pérez.
15 de enero de 2025.
Descripción:
Ejercicio 2, Parcial 3.
"""
def Imprimir_alumno(Nombre: str, Edad: int,Matricula: int,Grupo: int,Semestre: int)-> None:    # Definición de la función y tipo de datos.
    print("**DATOS PERSONALES**")
    print(f"Nombre: {Nombre} \nEdad: {Edad} \nMatricula: {Matricula} \nGrupo: {Grupo} \nSemestre: {Semestre} ")

def main() -> None:
    Nombre = "Rosalinda"
    Edad = 21
    Matricula = 1123132112
    Grupo = 303
    Semestre = 3

    Imprimir_alumno(Nombre,Edad,Matricula,Grupo,Semestre) # Llamada a la función imprimir_alumno.

if __name__ == "__main__":  # indica si el código es el que se ejecuta.
    main()  # Llamada de la función a nivel de módulo.'''



# Argumentos por nombre.
def Imprimir_alumno(Nombre: str, Edad: int,Matricula: int,*,Grupo: int,Semestre: int)-> None:   # El asterisco es de donde a donde debes especificar su nombre y valor.
    print(f"Nombre: {Nombre} \nEdad: {Edad} \nMatricula: {Matricula} \nGrupo: {Grupo} \nSemestre: {Semestre} ")

def main() -> None:
        Nombre = "Rosalinda"
        Edad = 21
        Matricula = 1123132112
        Grupo = 303
        Semestre = 3
        Imprimir_alumno(Nombre,Edad,Semestre,Grupo,Matricula)
        print()
        #Imprimir_alumno("Rosalinda",21,Grupo=303,Matricula= 1234,Semestre=3)
        print()
        #Imprimir_alumno("Rosalinda",21,Grupo=303,Matricula= 1234,Semestre=3)
        print()

main()

'''
# Valores por defecto: Se inicializa 
def Imprimir_alumno(Nombre: str, Edad: int,Matricula: int,Grupo: int,Semestre: int = 3)-> None:    # Definición de la función y tipo de datos.
    print("**DATOS PERSONALES**")
    print(f"Nombre: {Nombre} \nEdad: {Edad} \nMatricula: {Matricula} \nGrupo: {Grupo} \nSemestre: {Semestre} ")


def main() -> None:
    Nombre = "Jennifer"
    Edad = 19
    Matricula = 11233456
    Grupo = 303
    Semestre = 3

    Imprimir_alumno(Nombre,Edad,Matricula,Grupo,) # Llamada a la función imprimir_alumno.


if _name_ == '_main_':  # indica si el código es el que se ejecuta.
    main()  # Llamada de la función a nivel de módulo.
'''
"""
exámen
#Cuatro en raya
#El gato
#ahorcado
#Todo eso en un menú, en un solo programa.
"""