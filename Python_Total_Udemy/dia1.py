'''
Crea un código que imprima en pantalla la siguiente expresión (pero usando print una sola vez):

Línea 1
Línea 2
Línea 3
'''
#\n ----- cambio de línea
print("Línea 1\nLínea 2\nLínea 3")


'''
Crea un código que imprima en pantalla la siguiente expresión.

A	B	C
D	E	F
G	H	I
'''
#\t ---- tabulador
print("A\tB\tC\nD\tE\tF\nG\tH\tI")


'''
Crea un código que imprima en pantalla la siguiente expresión:

Barra Normal: /
Barra Invertida: \
'''
#\\ ------- \" también es una opción para que python lo incluya literalmente como parte de la string
print("Barra Normal: /\nBarra Invertida: \\")


'''
Crea un código que muestre en pantalla el nombre completo del usuario, permitiéndole ingresar su nombre y apellido con las siguientes instrucciones:

Escribe tu nombre:
Escribe tu apellido:
El código debe poder imprimir en pantalla el nombre y apellido del usuario, separados por un espacio.
'''
#combinar print con input
print(input("Escribe tu nombre: ")+ " " + input("Escribe tu apellido: "))