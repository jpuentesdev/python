cad = input('Dime un texto: ')
def txt_ascii(cadena):
    salida = []
    for i in cadena:
        salida.append(str(ord(i)))
    
    return ' '.join(salida)


print(txt_ascii(cad))


print(ord("P"))
