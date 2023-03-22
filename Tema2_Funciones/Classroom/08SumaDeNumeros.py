'''
8.- Suma de números
--------------------
Escriba un programa que solicite al usuario que ingrese 5 números, separados por comas. 

Calcule la suma de los 5 números y muestre los números ingresados y la suma al usuario.
'''

def suma_de5():
    print(f"El usuario ha elegido los siguientes 5 números: ")
    valores = []
    for i in range (5):
        entrada = input("Un numerito :")
        valores.append(int(entrada))
    valores.append(sum(valores))
    valores.append("Éste último es la suma total")
    return(valores)

print(suma_de5())




