cadena = "En un lugar de la Mancha..." #primero se define la cadena de texto
print(cadena)
print(len(cadena))

print(cadena.capitalize()) #() de dentro son necesarios por ser una función

print(cadena.swapcase()) #intercambiar mayúscula por minúscula

print(cadena.replace("la","lo")) #reemplazar "la" por "lo"

#F5 EJECUTAR EN LA CONSOLITA

print(cadena.title()) #la primera letra de cada palabra la pone en mayúscula

print(cadena.split()) #convertir cadena en una lista

trozos = cadena.split() #segunda forma de hacerlo
print(trozos)

cadena = "1,2,3,4,5,6,7"
trozos = cadena.split(',')
print(trozos)

unida = ".-".join(trozos) #une los trozos de la cadena con los separadores introducidos, siempre lleva antes el separador
print(unida)

print(cadena+unida)




#split
cadena = "esta es una tarde # estupenda para aprender python"
print(cadena)

palabras = cadena.split()
print(palabras)

#join
unidas = ".-.".join(palabras) #te devuelve la cadena con los elementos de separación indicados
print(unidas)

#find
posicion = cadena.find("#")
print(posicion)
print(cadena[ :posicion-1])
print(cadena[posicion+1:])