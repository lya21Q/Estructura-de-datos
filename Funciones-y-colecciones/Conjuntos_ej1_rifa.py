"""
Nombre: Rosalinda Aquino Pérez
Este programa es una rifa, en donde se registra el correo
electronico y solamente permite ingresar un correo por participante.

"""
import random


op = None
def menu():
    print("[1].- Ver correos de participantes:")
    print("[2].- Agregar correo de participante:")
    print("[3].- Eliminr correo de participante:")
    print("[4].- Seleccionar ganador")
    print("[0].- Salir:")
    op=int(input("Ingrese una opción:"))
    return op

correo_participante = set()# Se crea un conjunto vácio, utilizando la función set.
correo_eliminar = set()
def consultar_correo(op,correo_participante,correo_eliminar):
    while op != 0:#El ciclo va a iterar mientras op, sea diferente de cero.
        if op == 1:
            if len(correo_participante)==0:#Si el conjunto está vacio imprime un mensaje.
                print("No hay varticipantes paramostrar")
                print("--------------------------------------------")
            else:
                for correo in correo_participante:
                    print(f"El conjunto de correos son:")
                    print(f"{correo_participante} ")#si no lo está imprime el contenido del conjunto.
                    print("----------------------------------------------------")
        elif op == 2:
            correo_nuevo = input("Ingresa el correo de participante a agregar: ")#Solicita al usuario que ingrese su correo electronico.
            correo_participante.add(correo_nuevo)#Lo añade al conjunto.
            print(f"El correo{correo_nuevo} ha sido agregado correctamente. ")#Imprime un mensaje de que se ha añadido correctamente.
            print("------------------------------------------------------------------")
        elif op == 3:
            if(len(correo_participante)==0):#Si el conjunto está vacio, no hay nada que eliminar.
                print("No hay varticipantes para mostrar")#Imprime el letrero deonde indica que no hay participantes para borrar.
                print("--------------------------------------------")
            else:
                correo_eliminar = input("Ingrese el correo a eliminar: ")  # Si hay participantes, se solicita al usario que indique que correo desea eliminar.
                for correo in correo_participante:
                    correo_participante.remove(correo_eliminar)
                    print("El correo ha sido eliminado correctamente.")#Se imprime un mensaje indicando que el correo ha sido eliminado correctamente.
                    print("----------------------------------------------------")
        elif op==4:
            if(len(correo_participante)==0):
                print("No hay varticipantes paramostrar")
            else:
                random.choice(list(correo_participante))
                print(f"El correo ganador es: {correo_participante}")
                print("---------------------------------------------")
        elif op == 0:
            print("Saliendo del programa.")
            break
        else :
            print("Opción no válida")
    return correo_participante

op=menu()
correo_participante=consultar_correo(op,correo_participante,correo_eliminar)

