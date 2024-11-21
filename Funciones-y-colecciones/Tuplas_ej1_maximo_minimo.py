"""
Este programa muestra el valor máximo y mínimo de una lista de números. En este caso, la tupla se utiliza para devolver los valores máximo y mínimo de la función.

  ***  Valor máximo y mínimo de una lista de números del usuario  ***

1) Ver lista de números.

2) Añadir número a la lista.

3) Determinar el valor máximo y mínimo de la lista de números.

0) Salir.

Cualquier otro caso -> Opción no válida.

"""
op=None
lista=[]
numero=0
valor_minimo=0
valor_maximo=0
valores=0
while op!=4:
    print("Este programa muestra el valor máximo de una lista de numeros.")
    print("calculadora basica")
    print("[1].-Ver lista")
    print("[2].-: Añadir número ")
    print("[3].-: Determinar el valor máximo y mínimo de la lista de números ")
    print("[4].-: Salir")
    op = int(input("ingrese una opción:"))

    if op==1:
        print(f"La lista de números es: {lista}")
        if lista==None:
            print("La lista esta vacía")
    elif op==2:
        numero=int(input("Ingrese el nuevo valor para añadir:"))
        lista.append(numero)
        print("Se ha añadido el nuevo número ")
    elif op==3:
        lista = [valor_minimo, valor_maximo]
        valores = (lista)
        for numeros in lista:
        if numero <= valor_minimo:
            print((f"El valor minimo es{valores}"))
        elif numero >=valor_minimo:
            print(f"El valor maximo es:")
    elif op==4:
        print("Saliendo del programa")
    else :
        print("Opción no válida")
