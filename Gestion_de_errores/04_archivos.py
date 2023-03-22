'''
CUENTA LETRAS:
Hacer un programa que pida al usuario una serie de caracteres
Establecer manera de terminar
Cuando termine--- mostrar lista con las vocales y otra con las consonantes
además de decirle cuántas hay de cada una.
Los caracteres que no son letras se descartan
'''



vocales ="aeiou"
consonantes ="bcdfghjklmnñpqrstvwxyz"
lista_consonantes= []
lista_vocales= []

def cuenta_letras():
    while True:
        letra = input("Dime una letra: ")
        if letra == "":
            break
        if letra.lower() in consonantes:
            lista_consonantes.append(letra)
        elif letra.lower() in vocales:
            lista_vocales.append(letra)
    
    print(f"Consonantes: {len(lista_consonantes)}")
    print(lista_consonantes)

    print(f"Vocales: {len(lista_vocales)}")
    print(lista_vocales)

cuenta_letras()
        