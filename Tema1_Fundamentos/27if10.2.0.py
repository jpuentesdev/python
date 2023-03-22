'''
PROCEDIMIENTO 
17.342 € ----------500
-------------------200
-------------------100
-------------------50
-------------------20
-------------------10
-------------------5

'''





numero = 17342


lista=[17342]


if numero >=500:

    while numero>=500:
        numero-= 500
        lista.append(numero)
        print(numero)

    while numero>=200:
        numero-= 200
        lista.append(numero)
        print(numero)

    while numero>=100:
        numero-= 100
        lista.append(numero)
        print(numero)

    while numero>=50:
        numero-= 50
        lista.append(numero)
        print(numero)

    while numero>=20:
        numero-= 20
        lista.append(numero)
        print(numero)

    while numero>=10:
        numero-= 10
        lista.append(numero)
        print(numero)

    while numero>=5:
        numero-= 5
        lista.append(numero)
        print(numero)

    while numero>=2:
        numero-= 2
        lista.append(numero)
        print(numero)
else:
    while numero>=1:
        numero-= 1
        lista.append(numero)
        print(numero)

print(lista)

'''
elif centimetros < 9999 and centimetros >=100:
    print(f"{centimetros} cm {metros} m")
else :
    
    print(f"{centimetros} cm")
'''