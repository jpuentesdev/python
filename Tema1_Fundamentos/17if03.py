'''
03.EJERCICIO 03
Escribe un programa que pida por teclado en primer lugar el año actual y después un año
cualquiera. A continuación, el programa ha de indicar cuántos años faltan para llegar o
cuantos años han pasado al/desde ese segundo año.
'''

año1 = int(input("En qué año estamos: "))
año2 = int(input("Escribe otro año: "))
resta = año1 - año2
diferencia = año2 - año1


if año1 == año2:
    print("Son el mismo año")

elif año1 > año2:
    print(f"Desde el año {año2} han pasado {resta} años")

else:
    print(f"Para llegar al año {año2} faltan {diferencia} años")


#Desde el año 1997 han pasado 23 años.
#Para llegar al año 2025 faltan 5 años.