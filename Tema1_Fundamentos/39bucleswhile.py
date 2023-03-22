'''
Ejercicio anterior pero con diccionarios. Proceso de ir simplificando el código
'''

cadena = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

vocales = { "a":0, "e":0, "i":0, "o":0, "u":0}

letras ="aeiou"

for c in cadena.lower():
    if c in letras :
        vocales[c] +=1

print(vocales)


##################################################
vocales = {}

letras ="aeiou"

for c in letras:
    vocales[c] = cadena.lower().count(c) 

print(vocales)

    