'''
5.- Promedio
------------
En este ejercicio, creará un programa que calcule el promedio de una colección de valores ingresados por el usuario. 

El usuario ingresará 0 como valor centinela para indicar que no se proporcionarán más valores. 

Su programa debería mostrar un mensaje de error apropiado si el primer valor ingresado por el usuario es 0.

'''

import sys
def promedios():
    numeros = []
    promedio = 0
    count = 0
    total = 0
    print("Dame un número: ")
    entrada = int(sys.stdin.readline())
    while entrada != 0:
        count +=1
        numeros.append(entrada)
        print ("Dame otro número: ")
        entrada = int(sys.stdin.readline())
        total = sum(numeros)
        promedio = (total/count)
    
    else:
        print("La media de los números introducidos es las siguiente: ", promedio)

promedios()


#Diferencia entre input() y sys.stdin.readline()
#https://www.geeksforgeeks.org/difference-between-input-and-sys-stdin-readline/