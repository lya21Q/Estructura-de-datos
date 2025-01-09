"""
**Conversor a numeros enteros y flotantes
con válidación.
1)
2)
0)
"""
from uu import Error

from paramiko.common import ERROR

opcion=None
#TODO implementar menu
def menu():
    pass #La función pass indica que no hace nada por el momento.
#TODO implementar cadena a entero.
def cadena_a_entero(cadena):
    ...
#FIXME Revisar caso n=0

def cadena_a_flotante(cadena):
    raise NotImplementedError("Implementar función")

    while opcion!=0:
        if opcion==1:
            num_cadena=input("Ingresa un número a convertir")
            num=cadena_a_entero(num_cadena)
        elif opcion ==2:
            num_cadena=input("Ingresa un mumero a convertir.")
            num_cadena=cadena_a_flotante(num_cadena)
        elif opcion==0:
            print("Salir.")
