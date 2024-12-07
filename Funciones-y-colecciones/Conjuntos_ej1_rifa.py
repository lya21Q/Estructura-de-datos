"""
Nombre: Rosalinda Aquino Pérez
Este programa es una rifa, en donde se registra el correo
electronico y solamente permite ingresar un correo por participante.

"""

def menu(op):
    print("[1].- Ver correos de participantes:")
    print("[2].- Agregar correo de participante:")
    print("[3].- Eliminr correo de participante:")
    print("[4].- Seleccionar ganador")
    print("[0].- Salir:")
    return op

correo_participante=set()# Se crea un conjunto vácio, utilizando la función set.
def consultar_correo(op,correo_participante):
    if op == 1:
        if(correo_participante==0):
            print("No hay varticipantes paramostrar")
            print("--------------------------------------------")
        else:
            print(f"El conjunto de correos son: {correo_participante} ")
            print("----------------------------------------------------")
    if op == 2:
        correo_participante = input("Correo de los participantes: ")
        correo_participante.add()
        print(f"El correo{correo_participante} ha sido agregado correctamente. ")

    if op == 3:
        if(correo_participante==0):
            print("No hay varticipantes paramostrar")
            print("--------------------------------------------")
        else:
            print("----------------------------------------------------")
    if op==4:
        correo_eliminar=input("Ingrese el correo a eliminar: ")
        correo_participante.remove(correo_eliminar)
        print("El correo ha sido eliminado correctamente.")
        print("---------------------------------------------")
    if op == 0:
        print("Saliendo del programa.")
    return correo_participante

op=menu()
correo=consultar_correo(op)

