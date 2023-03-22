'''
Escribe un programa que pida dos números enteros, el segundo ha de ser mayor o igual
que el primero. A continuación, se debe mostrar por pantalla una lista con todos los
números enteros comprendidos entre los números introducidos, indicando en cada caso
si el número escrito es par o impar.
'''

num1 = int(input("Dame un numerito: "))
num2 = int(input("Dame otro numerito: "))

if num2< num1 or num2 == num1:
    print("El segundo número debe ser mayor que el primero")
else:
    for i in range(num1,num2):
        if i %2 ==0:
            print(f"{i} :")
            print(f"el número {i} es par")
        else:
            print(f"{i} :")
            print(f"el número {i} es impar")


