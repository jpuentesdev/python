'''
Validar DNI --- RECIBE NUM Y CALCULA LA LETRA
letras válidas: TRWAGMYFPDXBNJZSQVHLCKE
un dni será válido si:
    -Longitud de 8 numeros y 1 letra
    -Letra será válida si coincide con el índice de la división entera del número entre 23
'''

letras = "TRWAGMYFPDXBNJZSQVHLCKE"
def calcula_letra_dni(dni):
    valor = int(dni)
    division = valor % 23
    num = letras[division]
    return(num)

#print(calcula_letra_dni(1234567))

numeros ="123456789"
def valida_dni(dni):
    return len(dni) == 9 and calcula_letra_dni(int(dni[:8])) == dni[8].upper()

print(valida_dni("55000173C"))
