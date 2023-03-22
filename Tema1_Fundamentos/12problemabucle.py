#pedir a usuario un número, es par o impar?
numero = int(input("Dime un numero: "))

if numero %2== 0:
    print(f"El número {numero} es par")   #f---- convertir a cadena la variable
else:
    print(f"El número {numero} es inpar")
