"""
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

def decimal_a_binario_y_hexadecimal(op):
    if op == 1:
        numero = int(input("Ingrese el numero en base decimal: "))
        binario=""
        hexadecimal=""
        num=numero
        while num > 0:
            residuo= num % 2
            num=num // 2
            binario = str(residuo) + binario

        #convertir a hexadecimal.
        hexadecimal=""
        hexadecimal_1="0123456789ABCDEF"
        while numero > 0:
            residuo=numero % 16
            hexadecimal=hexadecimal_1[residuo]+ hexadecimal
            print(f"El numero {numero} es: {binario} en binario y {hexadecimal} slmllmdhexadecimal."return binario, hexadecimal
def binario_a_decimal_y_hexadecimal(op):
    if op == 2:
        binario = int(input("Ingrese el numero en base binaria: "))
        # conversion a decimal
        decimal = 0
        potencia = 0
        for digit in reversed(binario):
            decimal += int(digit) * (2**potencia)
            potencia += 1

        #coonversion hexadecimal
        hexadecimal = ""
        hexadecimal_1 = "0123456789ABCDEF"
        numero=decimal
        while numero > 0:
            residuo = numero % 16
            hexadecimal = hexadecimal_1[residuo] + hexadecimal
            numero = numero // 16
            print(f"El numero binario {binario} es: {decimal} en decimal y {hexadecimal} hexadecimal.")
        return decimal,hexadecimal

def hexadecimal_a_decimal_y_binario(op,numero,binario ):  #Convertir de hexadecimal a decimal
    if op==3:
        hexadecimal=input("Ingrese el numero en base hexadecimal: ")
        hexadecimal_1="0123456789ABCDEF"
        decimal=0
        potencia=0
        #Conversión de hexadecimal a decimal.
        for i in reversed(hexadecimal):
            valor=hexadecimal_1
            decimal+=valor*(16**potencia)
            potencia+=1

        #convertir de decimal a binario
        binario=""
        decimal=int(input("Ingrese el numero en base decimal: "))
        while numero > 0:
            residuo= numero % 2
            binario = binario + str(residuo) + binario
            numero/=2
            print(f"El numero hexadecimal {hexadecimal} es: {decimal} en decimal y {binario} en binario.")
    return decimal,binario

op=menu()
binario,hexadecimal=decimal_a_binario_y_hexadecimal(op)
decimal,hexadecimal=binario_a_decimal_y_hexadecimal(op,binario,hexadecimal)