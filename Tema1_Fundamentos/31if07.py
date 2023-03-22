'''
03.EJERCICIO 07
Escribe un programa que solicite los coeficientes de una ecuación de primer grado (a.x + b =
0), y que a continuación calcule y muestre como resultado la solución a la ecuación.

ax +b= 0
x= -b/a
'''



a = float(input("Escribe el valor de la variable a: "))
b = float(input("Escribe el valor de la variable b: "))

x = -b // a

if a == 0 and b == 0:
    print("Todos los números son solución")

elif a == 0:
    print("No tiene solución")

else:
    print(f"La solución es: {x}")


