import pprint
'''
#Bucles controlados por un contador    for
for variable   (inicio, fin, salto)



#Bucles controlados por una condición   while

'''

'''
for i in range(10): #acaba en 9
    print(f"la i vale {i}")

for i in range(20,50): #empieza en 20 y termina en 49
    print(f"la i vale {i}")

for i in range(20,50,2): #empieza en 20 y termina en 48, de dos en dos
    print(f"la i vale {i}")


for i in range(50,20,-2): #empieza en 50 y termina en 22, de dos en dos
    print(f"la i vale {i}")
'''


lista=[]
for i in range(20):
    lista.append(f'Elemento {i}')
pprint.pprint(lista)


#largo=len(lista)
#for i in range(largo):
#   print(lista[i])

#segundo modo
for x in lista:
    print(x)

