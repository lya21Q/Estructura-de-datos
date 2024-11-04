#Este programa imprime en consola los números separados por comas,
# del 1 hasta un número ingresado por el usuariio.

#Rosalinda Aquino Pérez

contador=1
#a) Solicite un número en consola.
print("**Licenciatura en Informática***")
numero=int(input(("Ingrese un número: ")))
while contador <= numero:
    if contador  % 3 == 0 and contador % 5 == 0:
        print("Licenciatura en informática"'\n', end=" ")
    elif contador  % 5 == 0 :
        print("Informática",",",end=" ")
    elif contador % 3 == 0 :
        print("Licenciatura ", end=" ")
    else :
        print(contador,",",end=" ")
    contador += 1