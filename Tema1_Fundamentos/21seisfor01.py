'''
Escribe un programa que utilizando el carácter producto (*), dibuje triángulos rectángulos
del tipo mostrado en el siguiente ejemplo. El programa necesitará conocer el número de
caracteres que forman los catetos.
'''
'''
Medida de los catetos: 4
*
* *
* * *
* * * *
'''
medida=5
simbolo="*\t"
for i in range(1,medida):
    print(simbolo* i)

print('\n\n')
################# hacer el triángulo al revés
medida =4
for i in range(medida,0,-1):
    print(simbolo* i)


