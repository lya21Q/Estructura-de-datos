"""Bienvenido al banco azteca"""

#consulta saldo
#ingresa dinero
#retirar dinero
#salir
#Elige una opción
op=1

while op != 7  :
    print("Bienvenido al banco azteca")
    print("[1].-Consulta Saldo: ")
    print("[2].-: Ingresa Dinero")
    print("[3].-: Retirar Dinero ")
    print("[4].-: Salir")

    saldo = int(input("ingrese saldo en cuenta: "))
    op=int(input("ingrese una opción: "))


    if op ==1 :
        print(f"Su saldo en cuenta es de {saldo}")
    elif op==2 :
        n1=int(input("ingresa la cantidad que deseas guardar: "))
        saldo= saldo + n1
        print(f"ahora tu saldo actual es de {saldo}")
    elif op==3 :
        numero1=int(input("ingresa la candidad que deseas retirar: "))
        print(saldo - numero1)
        print(f"ahora tu saldo actual es de {saldo}")
    elif op == 4:
        op = 4
        print("salio del programa")