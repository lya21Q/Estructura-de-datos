
#prueba_numero=int(input("Ingresa un número:"))
#print()
#cadena=input("Ingresa una cadena:").strip()
#print(cadena.isnumeric())
#print(cadena.isalpha())
#print(cadena.isalnum())
#numero=input("Ingresa un número:")
#while not numero.isnumeric():
 #   print("Opción no válida")
  #  numero=input("Intenta nuevamente:")
#print()
#numero=int(numero)
#print(f"El número {numero} es de tipo {type(numero)}")

def cadena_a_entero(cadena):
    no_puntos=cadena.count(".")#Contando el numero de puntos
    no_guiones=cadena.count("-")#Contando el numero de guiones
    revisar_cadena=cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in (0,1) and no_puntos in (0,1):
        return float(cadena)
    else:
        return None

num_cadena=input("Ingresa Z:")
numero=cadena_a_entero(num_cadena)

while numero is None:
    print("Opción no válida")
    num_cadena=input("Ingresa Z:")
    numero=cadena_a_entero(num_cadena)
print(f"El numero {numero} es tipo {type(numero)}")
