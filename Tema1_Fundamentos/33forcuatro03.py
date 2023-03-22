'''
Crea un programa que muestre la tabla del ejercicio número 1, utilizando bucles tipo for
con tipos range() que tengan solamente un argumento.

1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
20 23 26 29 32 35 38 41 44 47
10 14 18 22 26 30
40 35 30 25 20 15 10 5 0
'''

for i in range(11):
    print (f"{i} \t", end = '')  

print()

for i in range(10):
    print (f"{(i+1) *2} \t", end = '')   

print()

offset = 0
for i in range(10):
    print (f"{(20 + offset)} \t", end = '')
    offset +=3

print()

offset = 0
for i in range(6):
    print (f"{(10 + offset)} \t", end = '') 
    offset += 4

print()

offset = 0
for i in range(9):
    print (f"{(40 - offset)} \t", end = '') 
    offset  +=5
