'''
Nombre:
Fecha:
Descripción:
Ejemplos del uso de una tupla dentro de una función.
'''

""" Función que recibe una tupla con las calificaciones del semestre (tres calificaciones parciales y ordinario)
    y devuelve una tupla con el promedio de los parciales, el promedio final y si está aprobado """
def determinar_promedio(calificaciones):
    # Se calculan los promedios y se determina si está aprobado (promedio final mayor o igual a 6).
    promedio_parcial = sum(calificaciones[0:3])/len(calificaciones[0:3])
    promedio_final = (promedio_parcial + calificaciones[3])/2
    esta_aprobado = promedio_final >= 6

    # Regresa los valores en forma de una tupla. Nota: recordar que no se requiere el uso de paréntesis.
    return promedio_parcial, promedio_final, esta_aprobado


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
print("  ***  Programa que determina el promedio utilizando funcioens y tuplas  ***")

# Se solicitan las calificaciones de los parciales y ordinario.
parcial1 = float(input("Ingresa la calificación del Parcial 1: ").strip())
parcial2 = float(input("Ingresa la calificación del Parcial 2: ").strip())
parcial3 = float(input("Ingresa la calificación del Parcial 3: ").strip())
ordinario = float(input("Ingresa la calificación del Ordinario_Estructura_Datos: ").strip())
print()

# Se crea una tupla
calificaciones = (parcial1, parcial2, parcial3, ordinario)
print(calificaciones)
# Se utiliza la función para calcular los promedios y determinar si está o no aprobado.
# Para ello, se utiliza el desempaquetado de tuplas.
promedio_parcial, promedio_final, esta_aprobado = determinar_promedio(calificaciones)

if esta_aprobado:
    print("Felicidades, aprobaste!", end = " ")
else:
    print("Lo siento, no aprobaste.", end = " ")

print(f"El promedio de los parciales es: {promedio_parcial:.1f} y el promedio final es: {promedio_final:.1f}.")