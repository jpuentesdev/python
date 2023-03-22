# 1.CONDICIONALES ---- CONTROL DE FLUJO

# LOOPS (BUCLES)

# 2.LOOP FOR:
'''
A diferencia de otros lenguajes de programación, los loops for
en Python tienen la capacidad de iterar a lo largo de los
elementos de cualquier secuencia (listas, strings, entre otros),
en el orden en que dichos elementos aparecen.
'''
lista = ["a","b","c"]
for letra in lista:
    print(f"Letra: {letra}")
print("")

for l in lista:
    numero_letra = lista.index(l) + 1
    print(f"Letra {numero_letra}: {l}")
print("")


nombres = ["Pablo","Luis","Jose","penelope","patricia"]

for n in nombres:
    if n.lower().startswith("p"):
        print(n)
print("")


numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
print("")
print(f"Valor calculado directamente:\n{mi_valor}")
print("")


for a,b in [[1,2],[3,4],[5,6]]:
    print(a) #imprimer el primer caracter de cada sublista
print("")


# 3.LOOP WHILE:
'''
Podemos
pensar a los loops while como una estructura condicional que
se ejecuta en repetición, hasta que se convierte en falsa
'''

monedas = 5
while monedas >0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo más money")
print("")


respuesta = "s"
while respuesta == "s":
    respuesta = input("Quieres seguir? s/n: ").lower()
else:
    print("Gracias")
print("")

#Números divisibles del 0 al 50
numero = 50
while numero <= 50 and numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1
print("")
#PASS --- Guardar progreso del código sin dar error al depurar (quedándose congelado)

#BREAK --- Termina el programa
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for i in lista_numeros:
    if i >= 0:
        print(i)
    else:
        break # También se puede con "if else"
print("")
#CONTINUE --- Interrumpe iteración y la salta


#4.IN RANGE:
'''
La función range( ) devuelve una secuencia de números dados
3 parámetros. Se utiliza fundamentalmente para controlar el
número de ejecuciones de un loop o para crear rápidamente
una serie de valores
'''
lista = list(range(0,101)) 
print(lista)
print("")

#Múltiplos de 3 del 3 al 300
mi_lista = list(range(3,301,3)) 

#Suma todos los cuadrados de los números comprendidios entre 1 y 15
suma_cuadrados = 0
lista_numeros = list(range(1,16))
for num in lista_numeros:
    suma_cuadrados += num**2




#5.ENUMERATE
vocales = ["a","e","i","o","u"]

for indice, item in enumerate(vocales):
    print(indice,item)
print("")


mis_tuples = list(enumerate(vocales)) #creando lista de tuplas, formato (índice, caracter)
print(mis_tuples)
print(mis_tuples[2][0])  #imprimir el caracter en posición 3
print("")


texto = "Python"
lista_indices = list(enumerate(texto))
print(lista_indices)
print("")


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for names in lista_nombres:
    if names.startswith("M"):
        print(lista_nombres.index(names))
print("")



#6.ZIP:
'''
La función zip( ) crea un iterador formado por los elementos
agrupados del mismo índice provenientes de dos o más
iterables.

La función se detiene al cuando se agota el iterable con menor cantidad de elementos
'''

nombres = ["Valeria","Teo","Teodoro"]
edades = [26,77,34,55] #55 se ignoraría
ciudades = ["Lima","Madrid","Medellín"]
combinados = list(zip(nombres,edades,ciudades))

for nombre,edades,ciudades in combinados:
    print(f"{nombre} vive en {ciudades} y tiene {edades} años")
print("")


#7.MIN_MAX:
'''
La función min( ) retorna el item con el valor más bajo dentro
de un iterable. La función max( ) funciona del mismo modo,
devolviendo el valor más alto del iterable. Si el iterable contiene
strings, la comparación se realiza alfabéticamente(Teniendo en cuenta primero MAYÚSCULAS)
PONER .LOWER() PARA EVITAR ÉSTO ÚLTIMO
'''

ciudades_habitantes = {"Tijuana":1810645,
"León":1579803}

lista_valores = [5**5, 12**2, 3050, 475*2]

print(min(ciudades_habitantes.keys()))

print(max(ciudades_habitantes.values()))

print(max(lista_valores))
print("")


#8.RANDOM
#IMPORTANDO EL MÉTODO "RANDINT" DESDE LA LIBRERÍA "RANDOM"

#from random import randint
from random import * #importa todos los métodos de lalibrería
 
'''
Python nos facilita un módulo (un conjunto de funciones
disponibles para su uso) que nos permite generar selecciones
pseudo-aleatorias* entre valores o secuencias


randint(min, max): devuelve un integer entre dos valores dados (ambos límites incluidos)

uniform(min, max): devuelve un float entre un valor mínimo y uno máximo

random(sin parámetros): devuelve un float entre 0 y 1

choice(secuencia): devuelve un elemento al azar de una secuencia de valores (listas, tuples, rangos, etc.)

shuffle(secuencia): toma una secuencia de valores mutable (como una lista), y la retorna cambiando el orden de sus elementos aleatoriamente
'''

aleatorio = randint(1,50) #int aleatorio
print(aleatorio)

print(uniform(1,50)) #float aleatorio, mucha parte decimal
print(round(uniform(1,50),1)) #con único decimal

print(random()) # float aleatorio entre 0 y 1, mucha parte decimal, () VACÍOS

colores = ["azul","amarillo","verde","rojo"]
print(choice(colores)) #Elige un elemento al azar de una secuencia de valores

shuffle(colores)  #Devuelve una secuencia de valores cambiando el orden de sus elementos,   NON TYPE
print(colores) 
print("")



#9.COMPRENSIÓN DE LISTAS:
'''
La comprensión de listas ofrece una sintaxis más breve en la
creación de una nueva lista basada en valores disponibles en
otra secuencia. Vale la pena mencionar que la brevedad se
logra a costo de una menor interpretabilidad


ÚTIL EN FOR LOOPS --- MÉTODO APPEND()
'''

palabra = "python"
#FORMA YA CONOCIDA DE HACERLO
comprension_lista = []
for letra in palabra:
    comprension_lista.append(letra)

#FROMA POR COMPRENSIÓN DE LISTAS
lista_comprension = [letra for letra in palabra] #Igual que de la otra forma pero añadiento la variable interna (letra) delante y metiendo todo dentro de la lista
print(lista_comprension)
print("")

lista_comprension2 = [letra for letra in "python3"]
print(lista_comprension2)
print("")


lista_comprension3 = [n+1 for n in range(0,21,2)]
print(lista_comprension3)
print("")


lista_comprension4 = [n for n in range(0,21,2) if n*2 > 10] 
print(lista_comprension4)
print("")


#Si también hay un else:

lista_comprension5 = [n if n*2 >10 else "no" for n in range(0,21,2)]
print(lista_comprension5)
print("")


lista_comprension6_pies_a_metros = [n*3.281 for n in range(10,51,10)]
print(lista_comprension6_pies_a_metros)
print("")


temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n-32)*(5/9) for n in temperatura_fahrenheit]