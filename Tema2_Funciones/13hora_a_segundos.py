'''
Hacer una función que reciba una hora en formato hh:mm:ss
Debe devolver la cantidad de segundos de dicha hora
'''
#Hecha con un input
'''
def horas():
    list = []
    for i in range(3):
        num= int(input("Dame segundos, minutos y horas: "))
        list.append(num)
    print(f"El usuario ha introducido {list[0]} segundos {list[1]} minutos {list[2]} horas")
    horas_finales = list[0] + list[1]*60 + list[2] * 3600 
    list[0] = horas_finales
    print(f"{list[0]}:00:00 segundos")

horas()
'''

#Hecho con una hora dada en formato cadena
def segundos(cadena_hora):
    horas = cadena_hora[0:2]
    horas = int(horas)
    minutos = cadena_hora[3:5]
    minutos = int(minutos)
    segundos = cadena_hora[6:8]
    segundos = int(segundos)
    hora_inical = f"{horas}:{minutos}:{segundos}"
    print(hora_inical)
    horas_finales = horas * 3600 + minutos *60 + segundos
    print(horas_finales)  

segundos("23:24:24")
    



