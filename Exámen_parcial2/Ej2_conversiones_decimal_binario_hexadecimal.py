"""
Instrucciones:
Escribe un programa de nombre Ej2_conversiones_decimal_binario_hexadecimal.py que realice lo que se indica en la descripción del programa.
Comparte el enlace de GitHub en la caja de texto al final de la pregunta.
Descripción del programa:
Este programa convierte números entre las bases decimal, binaria y hexadecimal.
"""
op=None
def menu():
    print("***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print("[1].- Convertir de decimal a binario y hexadecimal.")
    print("[2].-convertir de binario a decimal y hexadecimal.")
    print("[3].-Convertir de hexadecimal a decimal y binario.")
    print("[0].- Salir.")
    op=int(input("Ingrese opción:"))
    return op
numero=None
def decimal_a_binario_y_hexadecimal(op,numero):
    binario=""
    if op==1:
        numero=int(input("Ingrese el numero en base decimal: "))
        while numero > 0:
            residuo= numero % 2
            decimal=numero / 2
            binario = str(residuo) + binario
            #convertir a hexadecimal.
            hexadecimal_1="0123456789ABCDEF"
            residuo=numero % 16
            hexadecimal=hexadecimal_1[residuo]+ hexadecimal
            print(f"El numero {numero} es: {binario} en binario y {hexadecimal} hexadecimal.")

    return numero, hexadecimal



def binario_a_decimal_y_hexadecimal(op,numero):
    decimal=0
    if op==2:
        decimal=int(input("Ingrese el numero en base binaria: "))
        while decimal > 0:
            print(f"El numero binario {numero} es: {numero} en decimal y {numero} hexadecimal.")

    return decimal



def hexadecimal_a_decimal_y_binario(op,numero):
    #Convertir de hexadecimal a decimal
    if op==3:
        hexadecimal=(input("Ingrese el numero en base hexadecimal: "))
        hexadecimal_1=("0123456789ABCDEF")
        decimal=0
        potencia=0
        for i in reversed(hexadecimal):
            valor=hexadecimal_1
            decimal+=valor*(16**potencia)
            potencia+=1

        #convertir de decimal a binario
        binario=""
        numero=decimal_a_binario_y_hexadecimal(op,numero)
        while numero > 0:
            residuo= numero % 2
            numero/=2

        print(f"El numero hexadecimal {numero} es: {numero} en decimal y {numero} en binario.")
    return decimal

op=menu()
decimal_a_binario_y_hexadecimal(op,numero)
binario_a_decimal_y_hexadecimal(op,numero)
hexadecimal_a_decimal_y_binario(op,numero)