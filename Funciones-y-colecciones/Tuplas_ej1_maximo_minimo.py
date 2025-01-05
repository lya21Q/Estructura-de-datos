'''
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción:
Ejercicio 1.
'''
op=None
#Muestra el menú al usuario.
def menu():
    print("Este programa muestra el valor máximo de una lista de numeros.")
    print("[1].- Ver lista")
    print("[2].- Añadir número: ")
    print("[3].- Determinar el valor máximo y mínimo de la lista de números ")
    print("[0].- Salir")
    #Solicita al usuario que ingrese una opción.
    op = int(input("Ingrese una opción:"))
    return op

lista=[]
valores=()
numero=0
maximo=None
minimo=None

def comparacion(op,valores,lista,maximo,minimo):
    while op!=0:
        #Opción par ver la lista..
        if op==0:
            print("Saliendo del programa.")
        elif op==1:
        #Opción para añadir número.
            if (valores)!=0:
                print(f"La lista de números es: {valores}{","}")
            else:
                print("No hay valores que mostrar.")
        #Caso para determinar el valor maximo y el minimo de la lsta de numeros.
        elif op==2:
            numero=float(input("Ingrese el número a la lista:"))
            lista.append(numero)
            valores=tuple(lista)
            print(f"El numero {numero} se agrego con éxito!. ")
        # Caso para determinar el valor máximo y el minímo de la lsta de numeros.
        elif op==3:
            if len(valores)!=0:
                maximo=valores[0]
                minimo=valores[0]
                for i in valores:
                    if i > maximo:
                        maximo=i
                    if i < minimo:
                        minimo=i
                print(f"El maximo es ,{maximo}")
                print(f"El valor minimo es:{minimo}")
            else:
                print("No hay valores para mostrar")
        else:
            print("Opcion no vàlida")
        op=menu()
    return valores
#Llamada de las funciones.
op=menu()
valores=comparacion(op,valores,lista,maximo,minimo)