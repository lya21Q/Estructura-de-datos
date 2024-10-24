#elif condición :
#codigo si condicion 2 es verdad
# <14 niños y adolescentes
#15 y 25 jovenés
#25 y 45 adultos jovenes
#46 y 60 adultos maduros
#>60 adultos mayores
#A que grupo de edad pertenece

edad=input("Ingrese la edad: ")
edad=int(edad)

if edad <= 14 :
    print("El numero esta en el rango de niños y adolescentes")
elif edad >=15 and edad  <= 25 :
    print("El numero esta en el rango de jovenes")
elif edad >=25 and edad <=  45 :
    print("El numero esta en el rango de adultos jovenes")
elif edad >= 46 and edad <=  60 :
    print("El numero esta en el rango de adultos maduros")
elif edad >= 60 :
    print("El numero esta en el rango de adultos maduros")
else :
  print("El rango pertenece a adultos mayores")



