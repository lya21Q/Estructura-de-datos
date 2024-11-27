"""
Ejercicio 1: Suma acumulativa.
Nombre : Rosalinda Aquino Pérez
"""
print("Programa que cálcula la suma acumulativa")
numero_f=int (input("Ingrese el número final: "))#Solicitamos al usuario que ingrese el número final hasta el cual desea calcular la suma.
print(f"La suma del 0 hasta el {numero_f}, es : ")
contador = 0#Inicializamos el contador en cero, el contador llevará un conteo de cero, hasta el número final que se ingrese.
aux = 0# inicializamos aux en cero, que llevara la suma acumulada de los valores del contador.

while contador <= numero_f :#Este bucle se ejecutara mientras contador sea menor o igual a numero final.
    aux += contador#sumamos el valor actual de contador a la variable aux.
    contador +=1
print(aux)#imprimimos el valor que contiene la variable aux.

