'''
Crea un programa que cree dibujos del tipo mostrado en el ejemplo. El programa ha de
preguntar por el número de filas que tenga la estructura:
Número de filas: 4
    ---*---
    --***--
    -*****-
    *******
'''



numero= int(input("Dime la altura del triángulo: "))
espacios=numero -1
caracteres=1

for i in range(numero):
    print("\t" * espacios + "*\t" * caracteres + "\t" * espacios)
    espacios -=1 #la próxima vez que se recorra se le restará 1
    caracteres +=2 #la próxima vez que se recorra se le sumará 2


#################### Hacerlo del revés

print()


numero = 4
espacios = 0
caracteres = numero *2-1
for i in range(numero):
    print("\t" * espacios + "*\t" * caracteres + "\t" * espacios)
    espacios +=1
    caracteres -=2







