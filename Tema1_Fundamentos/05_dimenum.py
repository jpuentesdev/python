#Entrada : pedimos un número al usuario

#Salida : "El doble de <20> son <40>"
#       "El cuadrado de 20 son <400>"


#Entrada
numero = input ("Dame un numero... : ")
entero = int(numero)
print(type(entero))
doble = 2 * entero
cuadrado = entero * entero

print("El doble de " , numero , "es " , doble)
print("El cuadrado de " , numero , "es " , cuadrado)



#opcion2
numero = input ("Dame un numero... : ")
entero = int(numero)

doble = 2 * entero
cuadrado = entero * entero

print("El doble de " + numero + "es " + str(doble)) #convierte de num a cadena y (int) de cadena a num  
print("El cuadrado de " + numero + "es " + str(cuadrado))


#recursos interesantes
raw=4 #te lo imprime en bruto lo que pongas
print( raw*4)

cadena = f"hola" #otro tipo de cadenas
num = 100
print ("Esto es un numero", num)
print (f"Esto es un numero {num}")


