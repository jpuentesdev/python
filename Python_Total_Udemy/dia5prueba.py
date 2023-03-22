def vocales(text):
    vocales_list = []
    for v in "aeiou":
        if v in text.lower():
           vocales_list.append(v)
    return vocales_list

print(vocales("Un pAjArito"))


def contar_vocales(text):
    dict = {}
    for v in "aeiou":
        if v in text.lower():
            dict[v] = text.count(v)

    return dict
print(contar_vocales("Ola mijo cómo están"))




'''
textillo = 'Pingüino: Málaga es una ciudad fantástica y en Logroño me pica el... moño'
a,b = 'áéíóúü','aeiouu'
trans = str.maketrans(a,b)

print(textillo.translate(trans))
'''


'''
textillo = "Áveces es mejór"

textillo = textillo.lower().replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
print(textillo)
'''
