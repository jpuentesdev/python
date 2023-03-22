'''
6.- Tabla de descuentos
-----------------------
Un minorista en particular tiene un 60 por ciento de descuento en una variedad de productos descontinuados.

Al minorista le gustaría ayudar a sus clientes a determinar el precio reducido de la mercancía al tener una tabla de descuentos impresa en el estante que muestre los precios originales y los precios después de que se haya aplicado el descuento. 

Escriba un programa que use un bucle para generar esta tabla, que muestre el precio original, el monto del descuento y el nuevo precio para compras de $4.95, $9.95, $14.95, $19.95 y $24.95. 

Asegúrese de que los montos de descuento y los nuevos precios se redondeen a 2 decimales cuando se muestren.

'''
#Haciendo una tabla 10x10
def pinta_tabla():
    tabla = [
        [1,2,3,4,5,6,7,8,9,0],
        [0,9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9,0],
        [0,9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9,0],
        [0,9,8,7,6,5,4,3,2,1],
    ]
    for f in tabla:
        for c in f:
            print(f"{c}\t", end="")
        print()

pinta_tabla()

#Creando código para tabla HTML
def la_tabla(filas,cols):
    cadena = "<table>"
    for f in range(filas):
        cadena += "<tr>"
        for c in range(cols):
            cadena += f"<td>({f},{c})</td>"
        cadena += "</tr>"
    cadena += "</table>"
    return cadena
print(la_tabla(10,10))




table = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
lista = [1,2,3,4]
print(lista[1])

print(table[1][1]) # fila 1, columna 1, la anterior fila y columna tienen el valor 0
#Dos formas de imprimir la tabla
for i in range(len(table)):
    for j in range(len(table[0])):
        print(table[i][j], end=" ")
    print()


for i in table:
    for j in i:
        print(j, end=" ")
    print()



