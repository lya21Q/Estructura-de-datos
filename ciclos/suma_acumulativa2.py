"""
Programa 2 :Suma acumulativa.
Rosalinda Aquino Pérez
21/11/2024
"""

print("Programa que calcula la suma acumulativa de dado un número inicial y uno final.")
numero_inicial=int(input("Ingrese el numero inicial:"))#Solicitamos al usuario que ingrese el número inicial y lo convierte a un valor entero.
numero_final=int(input("Ingrese el numero final:"))#Solicitamos al usuario que ingrese el número final y lo convierte a un valor entero.
print(f"El la suma acumulativa del numero {numero_inicial} hasta {numero_final} es:")

contador=0#Inicializa la variable contador en cero, que se utilizaremos para iterar desde 0 hasta numero final que ingrese el usuario.
aux=0#Inicializaremos la variable aux en cero, est variable nos ayudara a acumular las sumas.
while contador<=numero_final:#Este bucle se ejecutara mientras contador sea menor o igual a numero final.
    aux+=contador#sumamos el valor actual de contador a la variable aux.
    contador+=13#Aumentamos el contador en 1
print(aux)#Imprime el valor que contiene la variable aux, que es la suma acumulativa desde el valor inicial, al final.


