#Rosalinda Aquino Pérez
#Descripción del programa: Este programa realiza las operaciones básicas de una cuenta:
#1) Mostrar saldo.
#2) Ingresar dinero.
#3) Retirar dinero.
#0) Salir.
#Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

op=None #Variable que controlará las opciones.
saldo=0#Variable que controlará el saldo.
while op != 0  :
    #Muestra el menú al usuario.
    print("*** Bienvenido a tu cuenta de banco azteca ***")
    print("[1].-Consulta Saldo: ")
    print("[2].-: Ingresa Dinero")
    print("[3].-: Retirar Dinero ")
    print("[0].- Salir.")
    #Solicita al usuario que ingrese una opción.
    op=int(input("ingrese una opción: "))

    #Opción para consultar su saldo.
    if op ==1 :
        print(f"Su saldo en cuenta es de ${saldo :.2f}")
        print("---------------------------------------")
    #Opción para ingresar saldo.
    elif op==2 :
        n1=float(input("ingresa la cantidad que deseas guardar: "))
        saldo= saldo + n1
        print(f"Ahora tu saldo actual es de: ${saldo}")
        print("--------------------------------------")
    #Opción para retirar.
    elif op==3:
        print(f"Su saldo es : {saldo}")
        saldo_retirar=float(input("ingresa la candidad que deseas retirar: "))
        if saldo > saldo_retirar :
            saldo= saldo - saldo_retirar
            print("Se retiro exitosamente.")
        else :
            print(f"Tu saldo es insuficiente.")
    #Opción para salir del programa.
    elif op ==0:
        print("Fin del programa")
    else:
        print("Opción incorrecta")