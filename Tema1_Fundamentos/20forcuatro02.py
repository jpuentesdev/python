'''
Crea un programa que muestre el mismo resultado que en el ejercicio anterior, pero
utilizando ahora bucles tipo for con tipos range() de dos argumentos.
'''

    

for i in range(1,11):
    if(i//i==1):
        print (f"{i} \t", end = '')  

print()

for i in range(2,21):
    if(i % 2==0):
        print (f"{i} \t", end = '')   

print()

cadena = ''
for i in range(20,49):
    if i % 3 == 0: 
        i -=1
        cadena += str(i) + '\t'
print(cadena)   

print()

#metodo dos
cadena = []
for i in range(20,49):
    if i % 3 == 0: 
        i -=1
        cadena.append (str(i)) 

print(cadena)
#imprimirlo del revés   
resultado = cadena[::-1]
print(resultado)
#para que quede bonito, como el resto de filas
print('\t'.join(resultado))




print()

for i in range(10,31,4):
    print (f"{i} \t", end = '') 

print()

for i in range(40,-5,-5):
    print (f"{i} \t", end = '') 

