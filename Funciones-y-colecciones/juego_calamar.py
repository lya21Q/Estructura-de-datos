#Piedra papel o tijera.
from random import random, randint

opcion1=0
opcion2=0
op=None
def menu():
    print("Elige tu primer tiro:")
    print("[1].- Piedra. ")
    print("[2].- Papel.")
    print("[3].- Tijeras")
    print("[0].-Salir")
    print("-----------------------------")
    opcion1=int(input("Ingrese una opción:"))
    return opcion1

def menu2():
    print("Elige el segundo tiro.")
    print("[1].- Piedra. ")
    print("[2].- Papel.")
    print("[3].- Tijeras")
    print("[0].-Salir")
    print("-----------------------------")
    opcion2=int(input("Ingrese una opción:"))
    return opcion2


CPU=randint(1,3)
print(f"El CPU eligio: {CPU}.")
CPU_1=randint(1,3)
print(f"La segunda opción de CPU es:{CPU_1}")

while opcion1!=0 and opcion2!=0:
    if opcion1==0 and opcion2 == 0:
        print("Saliendo de l programa.")
    elif opcion1==1 and opcion2==2 and CPU==1 and CPU_1==2:
        print(f"El usuario eligio:{opcion1} y {opcion2}")
        print(f"CPU eligio {CPU} y {CPU_1}")
        eliminar=input("Elimina una opción: ")
    elif opcion1==2 and opcion2==3:
        print(f"El usuario eligio:{opcion1} y {opcion2}")
        print(f"CPU eligio {CPU},{CPU_1}")
        eliminar=input("Ingresa la poción que deseas eliminar. ")
    elif opcion1==3 and opcion2==1:
        print(f"El usuario eligio:{opcion1} y {opcion2}")
        print(f"CPU eligio {CPU},{CPU_1}")
        eliminar = input("Ingresa la poción que deseas eliminar. ")
    elif opcion1==3 and opcion2==3 and CPU==3 and CPU_1==3:
        print(f"El usuario eligio {opcion2} y {opcion1}")
        print(f"Cpu eligio: {CPU} y {CPU_1}")
        print("Es un empate.")
    else:
        print("Opción inválida.")
opcion1 = menu()
opcion2 = menu2()