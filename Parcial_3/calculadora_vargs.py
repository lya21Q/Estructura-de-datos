#Rosalinda Aquino Pérez
op=None
def menu():
    print("[1]. Sumar-")
    print("[2].-Multiplicar")
    print("[3].-Salir")
    op=int(input("Ingrese una opción:"))
    return op

def sumar(*vargs)->float:
    resultado=0
    for i in vargs:
        resultado+=i
    return resultado
print()

def multiplicacion(*vargs)->float:
    resultado=0
    for i in vargs:
        resultado=resultado*i
    return resultado

def cadena_flotante(cadena):
    no_puntos = cadena.cout('.')
    no_guiones = cadena.cout('-')
    revisar_cadena=cadena.lstrip('-').replace(".",'')
    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None
while op!=3:
    op=menu()
    if op==1:
        num1=input("Ingresa un numero flotante.")
        numero1=cadena_flotante()
        num2=input("Ingresa un numero flotante.")
        numero2=cadena_flotante()
    while num1 is None:
    print("Opción no válida, intente de nuevo.")
    print(f"El numero convertido es ahora:{numero1}")
    print(f"El numero convertido es ahora:{numero2}")

if __name__=="__main__":
    menu()