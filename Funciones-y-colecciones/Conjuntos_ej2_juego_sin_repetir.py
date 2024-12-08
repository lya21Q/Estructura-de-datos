"""
Nombre: Rosalinda Aquino Pérez
Este es un juego que se puede jugar de manera grupal, en donde el objetivo es decir palabras de un tema en específico y los jugadores deben tratar de no repetir la misma palabra.
Nota: no se debe mostrar las palabras en ningún caso. Además, se debe llevar un contador de la cantidad de palabras que llevan.

"""
op=None
def menu():
  print("Juego sin repetir")
  print("[1] mostrar las reglas del juego")
  print("[2] Presiona 'enter' para comenzar")
  opcion = input("Ingrese opción:")
  return op

palabras = set()
def contar_palabras(palabras):
  if op==1:
    for palabra in palabras:
      print(palabra)
  elif op==2:
    print()

