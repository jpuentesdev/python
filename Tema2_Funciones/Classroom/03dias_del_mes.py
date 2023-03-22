'''
La duración de un mes varía de 28 a 31 días. 

En este ejercicio, creará un programa que lea el nombre de un mes del usuario como una cadena. 

Entonces su programa debería mostrar el número de días en ese mes. 

Muestre "28 o 29 días" para febrero para que se aborden los años bisiestos.

'''

mes = str(input("Introduce un mes del año: ")).lower()
def dias_de_un_mes(mes):
    figuras = {"enero":"31 días","febrero":"28 o 29 días","marzo":"31 días","abril":"30 días","mayo":"31 días","junio":"30 días","julio":"31 días","agosto":"31 días","septiembre":"30 días","octubre":"31 días","noviembre":"30 días","diciembre":"31 días"}
    meses = ["enero","febro","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    if mes in meses:
        return (figuras[mes])
    else:
        return("Debes de introducir el nombre de un mes")

print(dias_de_un_mes(mes))