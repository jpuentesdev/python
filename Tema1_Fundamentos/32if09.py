'''
03.EJERCICIO 09
Escribe un programa que en primer lugar pregunte si se quiere calcular el área de un
triángulo o la de un círculo.
Si se contesta que se quiere calcular el área de un triángulo, el programa tiene que pedir
entonces la base y la altura y escribir el área.
Si se contesta que se quiere calcular el área de un círculo, el programa tiene que pedir
entonces el radio y escribir el área.
En ambos casos el programa debe ser capaz de calcular y mostrar el resultado adecuado.
'''
import math
variable = (input("triangulo o circulo: "))


if variable == "triangulo":
    base = int(input("Dame la base: "))
    altura = int(input("Dame la altura: "))
    area_triangulo= (base * altura) //2
    print(f"El area del triángulo es: {area_triangulo}")

elif variable == "circulo":
    radio = int(input("Dame el radio: "))
    area_circulo = math.pi * radio**2
    print(f"El area del circulo es: {area_circulo}")

else:
    print("Debe introducir (triangulo) o (circulo)")

