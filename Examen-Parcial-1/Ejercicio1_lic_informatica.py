#Este programa imprime en consola los números separados por comas,
# del 1 hasta un número ingresado por el usuariio.



contador=0

numero=int(input(("Ingrese un número:")))
while contador <= numero:
    if contador % 3==0 :
        print("Licenciatura")
        print(contador, end=" ")
    elif contador % 5 == 0 :
        print("Informatimática")
    elif contador % 3== 0 and contador % 5 == 0:
        print("Licenciatura en informatica")
        print()
    else :
        print(contador)
    contador += 1