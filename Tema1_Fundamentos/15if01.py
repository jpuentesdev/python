'''
03.EJERCICIO 01
Escribe un programa que pida por teclado dos números enteros. 
A continuación, el programa debe calcular su división, escribiendo el cociente entero,
en caso de que el resto no sea cero, habrá que mostrar también el valor del resto entero.
'''

dividendo = int(input("Escribe el dividendo: "))
divisor = int(input("Escribe el divisor: "))

resto = dividendo % divisor
cociente = dividendo // divisor

print("Divisor de números")

if divisor == 0:
    print("No se puede dividr por 0")

elif resto == 0:
    print(f"La división es exacta. Cociente:{cociente}")

else :
    print(f"La división no es exacta. Cociente:{cociente} Resto:{resto}")








 


