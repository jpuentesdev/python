################ juego tablero barquitos
import pprint
'''
tablero = []
for f in range(10):
    fila = []
    for c in range(10):
        fila.append(0)
    tablero.append(fila)

tablero[2][8] = 1
tablero[2][9] = 1




while True:
    barco_f = (input("Dime la fila (intro = FIN): "))
    if barco_f == "":
        break
    barco_f = int(barco_f)
    barco_c = int(input("Dime la columna: "))
    tablero[barco_f][barco_c] = 1


pprint.pprint(tablero)


objetivo_f = int(input("Dime la fila: "))
objetivo_c = int(input("Dime la columna: "))


if tablero[objetivo_f][objetivo_c] == 1:
    print("¡¡¡TOCADO!!!")
else:
    print("¡¡¡AGUA!!!")
'''

# Pasándolo a funciones
#1. función crear tablero
#2. Función pedir barcos
#3. función disparos 
#4. función verificar dispario

def crear_tablero():
    tablero = []
    for f in range(10):
        fila = []
        for c in range(10):
            fila.append(0)
        tablero.append(fila)
    return tablero


def pedir_barcos(tablero):
    while True:
        barco_f = (input("Dime la fila (intro = FIN): "))
        if barco_f == "":
            break
        barco_f = int(barco_f)
        barco_c = int(input("Dime la columna: "))
        tablero[barco_f][barco_c] = 1


def disparos(tablero):
    objetivo_f = int(input("Dime la fila: "))
    objetivo_c = int(input("Dime la columna: "))
    
    if tablero[objetivo_f][objetivo_c] == 1:
        print("¡¡¡TOCADO!!!")
    else:
        print("¡¡¡AGUA!!!")


def main():
    cuadro = crear_tablero()
    pedir_barcos(cuadro)
    pprint.pprint(cuadro)
    disparos(cuadro)

main()

