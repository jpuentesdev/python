'''
03.EJERCICIO 10
Escribe un programa que pida una distancia en centímetros y que Escribe esa distancia en
kilómetros, metros y centímetros (escribiendo solamente las unidades necesarias).
'''

centimetros = int(input("Dame una distancia en centímetros: "))


'''
Razonamiento:
El programa nos da un número en cm



'''

metros= centimetros /100
kilometros= centimetros / 10000



if centimetros >999999:
    print(f"{centimetros} cm {metros} m {kilometros} km")

elif centimetros < 9999 and centimetros >=100:
    print(f"{centimetros} cm {metros} m")
else :
    
    print(f"{centimetros} cm")


