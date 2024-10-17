expresion1=input("ingrese la expresion: ")
expresion2= input("ingrese la expresion: ")
expresion1= expresion1.lower()=="si"
print(expresion1)
expresion2= expresion2.lower()=="si"
print(expresion2)

print("f¿Ambas son verdaderas?: ",{expresion1 and expresion2})
print("f¿Ambas son verdaderas?: ",{expresion1 or expresion2})
print("f¿Ambas son verdaderas?: ",{not expresion1 })
print("f¿Ambas son verdaderas?: ",{not expresion2 })
