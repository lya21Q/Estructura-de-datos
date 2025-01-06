primer_parcial=float(input("ingrese la caficación parcial"))
primer_segundo=float(input("ingrese la caficación ordinaria"))
primer_tercero=float(input("ingrese la caficación final"))
primer_ordinario=float(input("ingrese la caficación final"))


def calificacion(calificaciones):
    sum=(calificaciones[0:2]/3)
    promedio_parcial=sum(calificaciones[3]/2)
    promedio_final=(promedio_parcial+calificaciones[3]/2)
    tupla_promedios=(promedio_parcial,promedio_final)
    return promedio_parcial,promedio_final

promedio_parcial,promedio_final=calificacion(calificaciones)