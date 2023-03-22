'''
03.EJERCICIO 10
Escribe un programa que pida un año y que determine si ese año es bisiesto o no.

Recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo
son, aunque los múltiplos de 400 sí.
'''

año = int(input("Dame un número: "))

if año % 400 and año % 100 == 0:
    print(f"{año} no es un año bisiesto")
elif año %4 == 0 or año % 400 == 0:
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")




 


