"""
Instrucciones:
Escribe un programa de nombre Ej2_conversiones_decimal_binario_hexadecimal.py que realice lo que se indica en la descripción del programa.
Comparte el enlace de GitHub en la caja de texto al final de la pregunta.
Descripción del programa:
Este programa convierte números entre las bases decimal, binaria y hexadecimal.
"""
def menu():
    print("***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print("[1].- Convertir de decimal a binario y hexadecimal.")
    print("[2].-convertir de binario a decimal y hexadecimal.")
    print("[3].-Convertir de hexadecimal a decimal y binario.")
    print("[0].- Salir.")
    op=int("Ingrese opción:")
    return op

def convertir_binario(op,numero):
    if op==1:
        numero=int(input("Ingrese el numero en base decimal: "))
        while binario>0:
            binario=str(numero % 2) + binario
            print(f"El numero {numero} es: {numero} en binario y {binario} hexadecimal.")

    return numero



def convertir_hexadecimal(op,numero):
    decimal=0
    if op==2
        decimal=int(input("Ingrese el numero en base binaria: "))
        print(f"El numero binario {numero} es: {numero} en decimal y {} hexadecimal.")

    return hexadecimal



def convertir_decimal(op,numero):
    if op==3:
        decimal=int(input("Ingrese el numero en base hexadecimal: "))
        print(f"El numero hexadecimal {numero} es: {numero} en decimal y {} en binario.")
    return decimal