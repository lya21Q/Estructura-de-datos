if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
    continuar = False  # si mi entrada es valida se detiene el ciclo
    numeros.append(float(numero))
    contador = contador + 1
else:
    print("Entrada no valida. Por favor ingrese un numero valido (entero o decimal) 😳")