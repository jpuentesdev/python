'''
Dos horas devolver diferencia 
'''

#No terminada
#Aprender a importar una función de otro archivo
def segundos(cadena_hora):
    horas = cadena_hora[0:2]
    horas = int(horas)
    minutos = cadena_hora[3:5]
    minutos = int(minutos)
    segundos = cadena_hora[6:8]
    segundos = int(segundos)
    horas_finales = horas * 3600 + minutos *60 + segundos
    print(horas_finales)  


def dif_horas(inicio,fin):
    diferencia = abs(segundos(fin)) - segundos(inicio)    #abs ---- numero entero(sin negativo)
    h = diferencia // 3600
    m = diferencia % 3600 // 60
    s = diferencia % 3600 %60

    return f"{h:02d}:{m:02d}:{s:02d}"
dif_horas("20:00:00","19:59:00")



    
