
ConjuntoA={11,4,10,9,5,11,15,7}
ConjuntoB={55,70,11,77,66,9,5}
#Operaciones básicas
print(ConjuntoA)
print(ConjuntoB)
union=ConjuntoA|ConjuntoB
print(union)
interseccion=ConjuntoA&ConjuntoB
print(interseccion)
diferencia=ConjuntoA-ConjuntoB
print(diferencia)
diferencia1=ConjuntoB-ConjuntoA
print(diferencia1)

lista_original=["Leon","Leopardo","Aguila","Gato","Capibara","Chapulin","Venado","Leopardo"]
print(lista_original)

conjunto_animales=set(lista_original)
print(conjunto_animales)

lista_modificada=list(conjunto_animales)
print(lista_modificada)

lista2=tuple(conjunto_animales)
print(conjunto_animales)

#ganador=randint->numero
#random.choice(lista)
