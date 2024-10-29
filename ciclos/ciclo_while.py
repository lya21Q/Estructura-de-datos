# while condición :
#solicitar un numero e imprimirlos hasta numero solicitado en consola
"""
Programa que imprime un ejemplo del ciclo while
"""
numero=int(input("Ingrese un número: "))
print(f"Los numeros del 1 al {numero} son:")
contador = 1

while contador <= numero :
    print(contador)
    contador +=1
#ejemplo 2
numero=int(input("Ingrese un número: "))
print(f"Los numeros del 1 al :, {numero} son:")
contador = 1

while contador <= numero :
    print(contador,end=" ")
    contador +=1
print()
print("Fin de cuenta")

#ejemplo 3
numero=int(input("Ingrese un número :"))
print(f"Los números pares de 1 al {numero} son: ")
contador = 2

if numero % 2==0 :
    while  contador <= numero :
        print(contador,end=" ")
        contador += 1

