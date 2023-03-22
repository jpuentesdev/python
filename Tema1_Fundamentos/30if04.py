'''
03.EJERCICIO 04
Escribe un programa que pida dos números enteros y que a continuación indique si el
número mayor es múltiplo del menor.
'''

num1 = int(input("Dame un número: "))
num2 = int(input("Dame otro número: "))

if num1 == 0 or num2 ==0:
    print("No se puede dividir entre 0")

elif num1 % num2 == 0 or num2 % num1 == 0 :
    if num1 > num2:
        print(f"{num1} es múltiplo de {num2}")
    else:
        print(f"{num2} es múltiplo de {num1}")
else:
    print("No hay números múltiplos")