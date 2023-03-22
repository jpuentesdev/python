'''
4.- Color de la casilla
-----------------------
Escriba un programa que lea una posición del usuario. 

Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. 

Luego usa la aritmética modular para informar el color del cuadrado en esa fila. 

Por ejemplo, si el usuario ingresa a1, su programa debería informar que el cuadrado es negro. 

Si el usuario ingresa d5, su programa debe informar que el cuadrado es blanco. 

Su programa puede suponer que siempre se ingresará una posición válida. 

No es necesario realizar ninguna comprobación de errores.

'''
posicion = input('Introduce la posicion en el tablero: ')
def ajedrez ():
	columna = posicion[0].lower()
	fila = int(posicion[1])
	letras = "aceg"
	if columna in letras:
		columnaempiezanegro = True
	else:
		columnaempiezanegro = False
	
	if columnaempiezanegro:
		if fila % 2 == 0:
			blanco = True
		else:
			blanco = False
	else:
		if fila % 2 == 0:
			blanco = False
		else:
			blanco = True
		
	if blanco:
		print("El cuadro es blanco")
	else:
		print("El cuadro es negro")

ajedrez()


