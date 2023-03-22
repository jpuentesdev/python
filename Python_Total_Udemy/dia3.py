#MÉTODO index()   ÍNDICE
'''
Las cadenas siempre empiezan por el índice 0
'''

texto = "hola"
#¿En qué posición está la letra "o"?
print(texto.index("o"))
#¿Qué caracter existe en determinada posición?
print(texto[1]) #se pueden poner números negativos, el "-1" sería el último caracter de la string

mi_texto = "Esta es una prueba"
mi_texto.index("a") #busca la posición de la primera "a" en la cadena
mi_texto.index("a",5) #busca la letra "a" a partir del espacio número 5
mi_texto.index("a",5,11) #busca la letra "a" a partir del espacio número 5 hasta el 10, 11 no inclusivo
mi_texto.rindex("a") #empieza a buscar desde la derecha


#EXTRAER SUB-STRINGS ---- SLICING STRINGS
mi_variable = "esta palabra será extraída"
print(mi_variable[5:12]) #obtener caracteres comprendidos entre esos espacios

texto="ABCDEFGHIJKLM"
fragmento = texto[:5] #desde el comienzo del string hasta la posición 5
print(fragmento)
fragmento = texto[2:10:2] #con salto 2
fragmento = texto[::-1] #la cadena del revés

'''
Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

print(frase[8::3])
'''
#MÉTODOS STRINGS:
#SEIS DE LOS MÁS DE TREINTA MÉTODOS QUE TIENE STRING

#MÉTODO .upper() pasa a mayúscula

#MÉTODO .lower() pasa a minúscula

#MÉTODO .split() separa un string en una lista de palabras
texto ="éste es el texto"
print(texto.split())
print(texto.split("t")) #separa a partir de las "t"

#MÉTODO .join()  une una lista en una string, con los separadores que elijas (lo contrario a split)
a ="Aprender"
b = "Python"
c = "es"
d = "genial"
e  =" ".join([a,b,c,d]) #convierte la lista en una cadena con el separador " "
print(e)

#MÉTODO .find() encontrar una sub-string
print(texto.find("t"))
print(texto.find("z")) # a diferencia de .index() si no encuentra el caracter, devuelve -1 en vez de dar error

#MÉTODO .replace() reemplazar parte de nuestra string por otra
text = "Hola mundo, ésto es una prueba de .replace()"
reemplazar = text.replace("o","a") #reemplaza todas las "o" por "a"
print(reemplazar)


#PROPIEDADES STRINGS:
'''
PROPIEDADES STRINGS: 

Son inmutables: una vez creados, no pueden modificarse sus partes, pero sí pueden reasignarse los valores de las variables a través de métodos de strings

concatenable: es posible unir strings con el símbolo +

multiplicable: es posible concatenar repeticiones de un string con el símbolo *

multilineales: pueden escribirse en varias líneas al encerrarse entre triples comillas simples (''' ''') o dobles (""" """)

determinar su longitud: a través de la función len(mi_string)

verificar su contenido: a través de las palabras clave in y not in. El resultado de esta verificación es un booleano (True / False).
'''

#LISTAS
#Todo lo visto sobre índices en strings aplica también para las listas 
#mi_lista[0] = "nuevo valor"
#mi_lista.append("prueba")
#mi_lista.pop(0) only index ------ si no introduces un índice borra el último elemento
# eliminado = mi_lista.pop(0)    así guardamos el valor del caracter eliminado
#mi_lista.sort()   ---- ordena los valores ------  type : NonType
#mi_lista.reverse()   ---- cambia el orden del revés----- type : NonType


#DICCIONARIOS
#NO sirven los índices para ellos
#NO puedes buscar valores en base a sus índices, puedes en base a sus claves
#BUENO PARA : Acceder a datos a partir de su relación con otro concepto en vez del orden en el que se introdujo.
diccionario = {"c1":55,"c2":["1","2","3"],"c3":{"valor1":27,"valor2":1085,"valor3":123}}
print(diccionario["c2"])

print(diccionario["c2"][1]) #imprime el valor del segundo caracter de la lista de la key "c2"

print(diccionario["c3"]["valor2"]) # la key del value seleccionado dentro de la key "c3"

diccionario["c4"] = "creando nuevos keys y values"
print(diccionario)

diccionario["c4"] = "sobreescribiendo el value de \"c4\""
'''
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
'''


#TUPLAS
'''
Los tuples o tuplas, son estructuras de datos que almacenan
múltiples elementos en una única variable. Se caracterizan por
ser ordenadas e inmutables. Esta característica las hace más
eficientes en memoria y a prueba de daños.

NO ES MUTABLE

¿Por qué tuplas en vez de listas?
    Ocupan menos espacios (eficiencia)
    A prueba de daños (no modificable)
'''
#Ésto se puede hacer con listas y diccionarios tmabién siempre que haya el mismo número de caracteres
mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print(a,b,c,d)



#SETS
'''
SON LISTAS DE ELEMENTOS ÚNICOS
Se diferencian de listas, tuplas y diccionarios porque son una colección
mutable de elementos inmutables, no ordenados y sin datos
repetidos
'''
#NO PUEDES INDEXARLOS
#NO admite listas ni diccionarios como elementos dentro, otra tupla sí
mi_set = {1,2,3,4,5,5,5,5,5,5,5}
print(mi_set)  #omite los elementos repetidos
s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1.union(s2) #forma de unir dos tuplas, siempre omitiendo elementos repetidos

s3.add(6) #añadir elemento
s3.remove(6) #eliminar elemento
s3.discard(7) #igual que remove(), pero si el elemento no existe no da error
s3.pop() #elimina elemento aleatorio (porque en las tuplas no hay índice)  IDEAL PARA HACER SORTEOS
s3.clear() #borrar elementos del set




#BOOLEANOS
'''
Los booleanos son tipos de datos binarios (True/False), que
surgen de operaciones lógicas, o pueden declararse
explícitamente.

BASES DE LA INTELIGENCIA ARTIFICAL

OPERADORES DE COMPARACIÓN
==
!=
>
<
>=
<=

OPERADORES LÓGICOS
and
or
not
'''

num = bool(5>6) #se puede omitir el "bool"
print(num)

lista = [1,2,3]
control = 5 in lista #Saldrá "False"

print(127/23 > 1000*50)