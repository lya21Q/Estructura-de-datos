"""
Ejercicio 1: Suma acumulativa.
Nombre : Rosalinda Aquino Pérez

"""
print("Programa que cálcula la suma acumulativa")
numero_f=int (input("Ingrese el número final: "))
print(f"La suma del 0 hasta el {numero_f}, es : ")
contador = 0
aux = 0 #Inicializamos el contador en cero.

while contador <= numero_f :#
    aux += contador
    contador +=1
print(aux)

