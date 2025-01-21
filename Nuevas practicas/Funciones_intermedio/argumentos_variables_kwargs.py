def preferencias(tema:str,**kwargs):
    print(f"E tema es:{tema}")
    for key,value in kwargs.items():
        print(f"Nombre: {key} prefiere {value}")

if __name__=="__main__":
    preferencias("Comida",Rebeca="Mole",Juan="Tacos",Bryan="Tlayudas",Jammileth="Tamales")
    #Ejemplo:
    #promedio("Galilea",ED=20,DyE:20)