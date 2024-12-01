'''
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción:
Ejemplos de uso de las Tuplas.
'''
#crear una lista
#Alumnos =[]
from os import remove

alumnos=["Addi","Jesus Alberto","Juan"]
alumnos.append("Hector")
print(alumnos)
print(alumnos[1])
alumnos.insert(0,"Tania")
print(alumnos)

for alumno in alumnos :
    print(alumno,end=" ")
    #remove("Hector")#Eliminar por valor
    for alumno in alumnos :
        print(alumno)
    #delet=(2)
print()
