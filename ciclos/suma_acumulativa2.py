"""
Programa 2 :Suma acumulativa.
Rosalinda Aquino Pérez
21/11/2024
"""

print("Programa que calcula la suma acumulativa de dado un número inicial y uno final.")
numero_inicial=int(input("Ingrese el numero inicial:"))
numero_final=int(input("Ingrese el numero final:"))
print(f"El la suma acumulativa del numero {numero_inicial} hasta {numero_final} es:")

contador=0
aux=0
while contador<=numero_final:
    aux+=contador
    contador+=1
print(aux)


