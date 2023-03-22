'''
Calcula la cantidad de billetes de cada tipo que te dará el banco para una cantidad de 17.342€
'''

import pprint
monedas = [500,200,100,50,20,10,5,2,1]
numero= 17342

desglose = {}

for m in monedas:
    desglose[m]= (numero // m)
    numero = numero % m

pprint.pprint(desglose)

print("")

print(f"La cantidad {numero} se desglose en:")
for k,v in desglose.items():
    if v >=0:
        print(f"{k} X {v}")