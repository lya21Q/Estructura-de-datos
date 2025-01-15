def saludar(nombre)-> str | None:
    print(f"hola,{nombre}")


if __name__ == "__main__":
    cadena = input("ingresa el nombre del usuario:")
    saludar(cadena)