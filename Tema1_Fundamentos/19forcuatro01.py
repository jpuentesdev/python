'''
Utilizando cinco bucles tipo for y en cada uno de ellos el tipo range() con tres argumentos,
escribe el código Python necesario para que se muestre por pantalla la siguiente
información tabulada con las siguientes cinco series aritméticas:
'''
'''
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
20 23 26 29 32 35 38 41 44 47
10 14 18 22 26 30
40 35 30 25 20 15 10 5 0
'''

# \t tabulador, \n salto de linea
#def mis_listas():
    #lista
n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=" ")

print()


for i in range(1,11):
    print (f"{i} \t", end = '')  #, end= '' para pasar de \n a \t

print()

for i in range(2,21,2):
    print (f"{i} \t", end = '')   

print()

for i in range(20,48,3):
    print (f"{i} \t", end = '')

print()

for i in range(10,31,4):
    print (f"{i} \t", end = '') 

print()

for i in range(40,-5,-5):
    print (f"{i} \t", end = '') 













