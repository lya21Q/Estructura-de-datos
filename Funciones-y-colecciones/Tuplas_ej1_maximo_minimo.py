'''
Nombre:Rosalinda AAquino Pérez
Fecha:21/11/2024
Descripción:
Ejercicio 1.
'''
op=None

def menu():
    print("Este programa muestra el valor máximo de una lista de numeros.")
    print("[1].- Ver lista")
    print("[2].- Añadir número: ")
    print("[3].- Determinar el valor máximo y mínimo de la lista de números ")
    print("[0].- Salir")
    op = int(input("Ingrese una opción:"))
    return op
lista=[]
valores=()
numero=0
def comparacion(op,valores,lista):
    while op!=0:
        if(op==1):
            if not valores:
                print("No hay números para mostrar.")
            else:
                print(f"La lista de números es: {valores}")
        elif(op==2):
            numero=float(input("Ingrese el nuevo valor para añadir:"))
            lista.append(numero)
            valores=tuple(lista)
            print(f"El numero {numero} se agrego con éxito!. ")
        elif(op==3):
            valor_minimo = None
            valor_maximo = None
            for i in lista:
                if(lista>valor_maximo):
                    valor_maximo==numero
                if numero < valor_minimo:
                    valor_minimo=numero
                    print(f"El valor minimo es : {valor_minimo}")
                    print(f"El valor maximo es : {valor_maximo}")
        elif(op==0):
            print("Saliendo del programa.")
        else:
            print("Opcion no vàlida")
    return valores

op=menu()
valores=comparacion(op,valores,lista)