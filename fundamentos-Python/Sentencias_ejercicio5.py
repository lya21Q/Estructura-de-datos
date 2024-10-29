'''
Nombre:Rosalinda Aquino Pérez
Fecha: 28/Octubre/2024
'''
print("Este programa determinará el promedio de una materia e indicará si el alumno aprobó o no la materia.")

cali_1=int(input("Ingrese la calificación del primer parcial: "))
cali_2=int(input("Ingrese la calificación del segundo parcial: "))
cali_3=int(input("Ingrese la calificación del tercer parcial: "))
ordinario=int(input("Ingrese la calificación del ordinario: "))

prom = (cali_1 + cali_2 + cali_3 + ordinario ) / 4
if prom >=6 :
    print(f"la calificación final es de {prom:.2f}, ¡Felicidades aprobaste! ")
else :
    print(f"la calificación final es de {prom:.2f}, Lo sentimos no aprobaste ")
