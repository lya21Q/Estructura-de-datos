"""Bienvenido al banco azteca"""

#consulta saldo
#ingresa dinero
#retirar dinero
#salir
#Elige una opción
op=None
saldo=100
while op != 0  :
    print("Bienvenido al banco azteca")
    print("[1].-Consulta Saldo: ")
    print("[2].-: Ingresa Dinero")
    print("[3].-: Retirar Dinero ")
    print("[0].-: Salir")

    op=int(input("ingrese una opción: "))

    if op ==1 :
        print(f"Su saldo en cuenta es de {saldo}")
    elif op==2 :
        n1=int(input("ingresa la cantidad que deseas guardar: "))
        saldo= saldo + n1
        print(f"ahora tu saldo actual es de {saldo}")
    elif op==3 :
        print(f"Su saldo es : {saldo}")
        numero1=int(input("ingresa la candidad que deseas retirar: "))
        if saldo < numero1 :
             print("Tu saldo es insuficiente")
        else :
            print(f"tu saldo actual es : {saldo - numero1}")
    elif op == 0:
        op = 0
        print("salio del programa")