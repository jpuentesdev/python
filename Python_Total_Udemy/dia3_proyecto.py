#ANALIZADOR DE TEXTO
'''
Pedir a usuario que ingrese un texto
Pedir al usuario que ingrese tres letras
El programa devolverá:
¿Cuántas veces aparecen las letras dentro del texto?
    1.método de strings para calcular cuántas veces aparece un sub-string
    2.Tener en cuenta las mayúsculas
¿Cuántas palabras hay en total en todo el texto?
    1.Convertir string en lista de sus palabras
    2.Utilizar método que las cuente
¿Cuál es la primera y última palabra del texto?
¿Cómo quedaría el texto en orden inverso?
    1.Unir elementos de una lista con espacios de intermedio
¿Aparece la palabra python en el texto?
'''

entrada = input("Por favor usuario, introduzca su texto favorito: ").lower()
letra1 = input("Dame la primera letra: ").lower()
letra2 = input("Dame la segunda letra: ").lower()
letra3 = input("Dame la tercera letra: ").lower()
letters_list = [letra1,letra2,letra3]

print(f"Ha escogido las siguientes letras: {letters_list}")
print("\n")
#1
print(f"La letra '{letra1}' aparece {entrada.count(letters_list[0])} veces en el texto\nLa letra '{letra2}' aparece {entrada.count(letters_list[1])} veces en el texto\nLa letra '{letra3}' aparece {entrada.count(letters_list[2])} veces en el texto")
print("\n")
#2
palabras = entrada.split(" ")
print(palabras)
print(f"En todo el texto hay {len(palabras)} palabras")
print("\n")
#3
print(f"La primera palabra del texto es '{palabras[0]}'\nLa última es '{palabras[-1]}'")
print("\n")
#4
reverso = palabras.copy()
reverso.reverse()
reverso_string = " ".join(reverso)
print(f"El texto del revés quedaría de la siguiente manera: {reverso_string}")
print("\n")
#5
py = "python".lower()
if py in entrada:
    print("El texto contiene la palabra 'PYTHON'")
else:
    print("El texto no contiene la palabra 'PYTHON'")
