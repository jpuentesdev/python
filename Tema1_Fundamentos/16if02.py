'''
03.EJERCICIO 02
Escribe un programa que pida por teclado dos números y que indique cuál de ellos es el menor
y cuál el mayor o bien si ambos números son iguales.
'''

num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe otro número: "))

print("Comparador de números")

if num1 == num2:
    print("Los dos números son iguales")

elif num1 > num2:
    print(f"Menor:{num2} Mayor:{num2}")

else:
    print(f"Menor:{num1} Mayor:{num2}")
