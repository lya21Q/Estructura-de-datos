def saludar(cadena)->str |None:
    print(f"Hola:{cadena}")

if __name__ == "__main__":
    cadena = input("Ingresa el nombre:")
    saludar(cadena)