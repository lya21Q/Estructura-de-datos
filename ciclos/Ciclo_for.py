#ESTRUCTURA del ciclo FOR:
#for variable in secuencia :
cadena=input("ingresa una cadena : ")
contador_caracteres=0
for caracter in cadena: #palabra reservada caracter
    contador_caracteres+=1
    print(f"{caracter}",end=" ")
print()
print(contador_caracteres)

alumnos=["Rosalinda", "Juan","Durán","Tania",
         "Bryan","Rebeca","Jennifer","Hector","Galilea","Patricia","Jesus","Addi"]
for alumno in alumnos : #palabra reservada alumno
    print(f" HOLA {alumno}")
print()

for i in range (1,10):#Range pide dos valores, inicio/fin. i palabra reservada
    print(i,end=",")
