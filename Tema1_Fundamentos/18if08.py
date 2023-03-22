'''
03.EJERCICIO 08
Escribe un programa que pida los coeficientes de una ecuación de segundo grado (a x2 + b x
+ c = 0) y que a continuación muestre la/s soluciones.

Una ecuación de segundo grado puede no tener solución, tener una solución única,
tener dos soluciones o que todos los números sean solución.
'''

from cmath import sqrt


a = int(input("Escribe el valor de la variable a: "))
b = int(input("Escribe el valor de la variable b: "))
c = int(input("Escribe el valor de la variable c: "))

disc= b * b - 4 * a * c
if disc <0:
    print("La ecuación no tiene solución")
else:
    raiz= sqrt(disc)
    x_1 = (-b + raiz) / (2 * a)            
    if disc != 0:
         x_2 = (-b - raiz) / (2 * a)        
         print(f'Dos soluciones {x_1} y {x_2}.')
    else:
         print(f'La única solución es x = {x_1}')