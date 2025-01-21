def colores_favoritos(persona:str,*varggs):
    print(f"{persona}:{varggs}")#Tupla


if __name__=="__main__":
    colores_favoritos("Jennifer","Morado","Negro","Blanco","Rosa")
    colores_favoritos("Addi","Azul","Blanco","Negro")
if __name__=="__main__":
    colores_favoritos("Rosalinda","Café")
    cadena="Hola"
    tupla="hola",
    print(cadena)
    print(tupla)

def sumar(*vargs)->int:
    resultado=0
    for i in vargs:
        resultado+=i
        print()
    return resultado
resultado=sumar(5,3,4)
print(f"El resultado es:{resultado}")

def sumar(*vargs)->int:
    resultado=0
    for i in vargs:
        resultado+=i
        print()
    return sum(vargs)
