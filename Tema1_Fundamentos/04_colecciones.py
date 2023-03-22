#colecciones: elementos que contienen un conjunto de valores, estructuras de datos básicas, que vienen incluidas con python

#TIPOS(más utilizadas):         type(x)--- saber que tipo de función es
#string
cadena="hola carola"
#list
#pueden contener cualquier cosa

lista= ["p","o"] #la más cómoda y la que más vamos a utilizar                                                                                     
lista = list((1,2,3)) 
lis=[]
lis.append("hola") #adjuntas a la lista "hola"--------- ['hola]
lis.append(1) #va metiendo textos de uno en uno---------- ['hola', 1]--------- .append(1)-- sin comillas porque es un número
lis.clear() #borrar todo el contenido de la lista
len(lis) #saber la longitud de la lista
lis.pop() #te devuelve el último elemento y lo elimina de la lista
lis.count() #cuenta cuantos elementos iguales hay en una lista---- lis.count(6)---- te duce cuantos 6 hay en la lista

cadena= "esta es una tarde estupenda para aprender python"
trozos = cadena.split()
trozos.count("es") #te saldría 1

sum(lis) #te suma la lista
max(lis) #máximo de la lista
min(lis) #mínimo de la lista

l1=["a","b","c"]
l2=[1,2,3,4]
l3=l1+l2 #resultado = ['a','b','c', 1, 2, 3, 4]



#dict
#tpl (tuplas)
#las listas son mutables y las tuplas son inmutables (como las cadenas), es recorrible (se puede sumar por ejemplo, pero no modificarla)
tpl= (1,2,3)
list(tpl) #cambia la tupla a lista
# #sets 