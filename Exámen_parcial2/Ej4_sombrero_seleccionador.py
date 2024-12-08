"""
Descripción del programa:
Este programa es un test de la elección del sombrero seleccionador de Harry Potter para alguna de las casas: Gryffindor, Slytherin, Hufflepuff y Ravenclaw.
"""

def menu():
    print("***  Ejercicio 4. Test del sombrero seleccionador de Harry Potter.  ***")
    print("[1].- Iniciar test.")
    print("[0] Salir.")
    op=int(input("ingrese opción"))
    return op

Gryffindor=0
Slytherin=0
Hufflepuff=0
Ravenclaw=0
preguntas=[]
def determinar_casa(op,preguntas,respuesta):
    if op==1:
        print("¿Cuál de las siguientes opciones odiarías más que la gente te llamara?")
        while respuesta!=4:
            print("1)-Ordinario.")
            print("2)-Ignorante.")
            print("3)- Cobarde.")
            print("4)- Egoísta.")
            respuesta=input("Seleccione su respuesta:")

        print("Despùes de tu muerte,¿que es lo que màs te gustaria que hiciera la gente cuando escuche tu nombre:")
        print("1)  - Te extraña, pero sonrie.")
        print("2)- Pidde màs historias sobre tus aventuras.")
        print("3)- Piensa con admiraciòn tus logros.")
        print("4)-No me importa lo que piensen de mì despues de mi muerte, lo que piensen de mì ahora es lo que cuenta.")
        respuesta=input("Seleccione su respuesta:")

        print("Dada la opción, preferirías inventar una poción que garantizara:")
        print("1) - Gloria.")
        print("2) - Sabiduría.")
        print("3) - Amor.")
        print("4) - Poder.")
        respuesta=input("Seleccione su respuesta:")

        print("¿Cómo te definirías en una sola palabra?")
        print("1) - Valiente.")
        print("2) - Ambicioso.")
        print("3) - Leal.")
        print("4) - Curioso.")
        respuesta=input("Seleccione su respuesta:")

        print("¿Qué cualidad te describe mejor?")
        print("1) - La fuerza.")
        print("2) - La astucia.")
        print("3) - La paciencia.")
        print("4) - La inteligencia.")
        respuesta=input("Seleccione su respuesta:")

        print("¿Cuál es tu clase favorita?")
        print("1)  - Vuelo.")
        print("2) - Defensa contra las artes oscuras.")
        print("3) - Animales fantásticos.")
        print("4) - Pociones.")

        print("¿Cuál es tu lenguaje de programación favorito?")
        print("1)- C.")
        print("2)- Python.")
        print("3) - C + +.")
        print("4)- JavaScript.")
