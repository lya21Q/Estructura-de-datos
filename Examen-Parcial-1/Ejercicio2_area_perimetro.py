print("Este programa determina el área y el perimetro de un rectángulo o de un círculo")
#Rosalinda Aquino Pérez
#03 Noviembre 2024
op=0
while op != 4  :
    # a) Muestre el menú anterior en consola.
    print("Programa que cálcula el área y el perímetro")
    print("[1].-Calcular el área de un rectágulo: ")
    print("[2].-: Calcular el perimetro de un rectángulo")
    print("[3].-: Calcular el área de un círculo ")
    print("[4].-: Calcular el perímetro de un círculo")
    print("[0].-: Salir")
    op=int(input("ingrese una opción: "))


    if op ==1 :
        # b) En caso de calcular un área o perímetro, solicite al usuario los valores requeridos (flotantes).
        base=float(input("Ingrese cuanto mide la base : "))
        altura = float(input("Ingrese cuanto mide la altura : "))
        area=base*altura #Realiza la operación.
        print(f"El área del rectangulo es : {area: .3f}")#Imprime el valor con tres decimales.

    elif op==2 :
        base=float(input("Ingrese cuanto mide la base : "))
        altura = float(input("Ingrese cuanto mide la altura : "))
        perimetro=base+base+altura+altura
        print(f"El périmetro es: {perimetro:.3f}")#d) Imprima el resultado en la consola. Nota: muestre únicamente 3 decimales en todos los casos.
    elif op==3 :
        pi=3.1416
        radio=float(input("Ingrese el radio : "))
        area=pi*radio**2
        print(f"El area es : {area:.3f}")
    elif op==4 :
        pi = 3.1416
        radio = float(input("Ingrese el radio : "))
        perimetro = (radio*2) *pi
        print(f"El area es : {perimetro:.3f}")
    elif op ==0:
        print("Saliendo del programa")
        break #Para finalizar el programa.
    else :
        print("Opción inválida")
        op=0