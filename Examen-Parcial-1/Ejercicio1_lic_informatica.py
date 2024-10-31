#Este programa imprime en consola los números separados por comas,
# del 1 hasta un número ingresado por el usuariio.

#Rosalinda Aquino Pérez

contador=0

numero=int(input(("Ingrese un número:")))
while contador <= numero:
    if contador % 3==0 and contador % 5==0:
        print(contador,"Licenciatura",contador, end=" ")
    elif contador % 5 == 0 :
        print("Informática", end=" ")
    elif contador % 3== 0:
        print("Licenciatura en informatica",contador, end=" ")
    else :
        print(contador,end=" ")
    contador += 1