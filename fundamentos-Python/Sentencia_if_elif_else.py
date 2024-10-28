'''
Nombre:
Fecha:
Descripción:
Uso de la sentencia de control if - elif - else.
'''

"""
La sentencia elif es una extensión del if-else y permite evaluar múltiples condiciones de forma secuencial. 
Es como tener varias opciones a elegir, ejecutándose el bloque de código correspondiente a la primera condición 
que sea verdadera.

Sintaxis:

if condicion_1:
    # Código a ejecutar si la condición_1 es verdadera.

elif condición_2:
    # Código a ejecutar si la condición_2 es verdadera.
  .
  .
  .
else:
    # Código que se ejecuta si todas las condiciones fueron falsas.
"""

# Ejemplo que determina el grupo al que pertenece de acuerdo a su edad.
print("  ***  Programa que determina el grupo de acuerdo a la edad  ***")
edad = int(input("Ingresa tu edad: "))

# lógica para determinar el grupo usando la estrucutra if-elif-else
if edad < 14:
    grupo = "Niños y adolescentes"

elif 15 <= edad < 25:
    grupo = "Jóvenes"

elif 25 <= edad < 45:
    grupo = "Adultos jóvenes"

elif 45 <= edad < 60:
    grupo = "Adultos maduros"

else:
    grupo = "Adultos mayores"

print(f"El grupo al que perteneces es: {grupo}.")

###############################################
"""
MODO DEPURACIÓN (DEBUG)

Utilizar ahora el modo depuración.
1) Crear un punto de ruptura en la variable edad. Marcar el número de línea y se pondrá un círculo color rojo.
2) Clic derecho y ejecutar el modo Debug.
3) Observar la nueva pantalla e ir ejecutando paso-a-paso (step over) F8.
4) Observar el comportamiento.
"""