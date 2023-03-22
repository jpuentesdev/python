'''
7.- Precio de la entrada
------------------------

Un zoológico en particular determina el precio de la entrada según la edad del visitante. 

Los huéspedes de 2 años de edad y menos se admiten sin cargo. 

Niños entre 3 y 12 años cuestan $14.00. 

Las personas mayores de 65 años o más cuestan $ 18.00. 

La entrada para todos los demás invitados es de $23.00.

Cree un programa que comience leyendo las edades de todos los invitados en un grupo del usuario, con una edad ingresada en cada línea. 

El usuario ingresará una línea en blanco para indicar que no hay más invitados en el grupo. 

Luego, su programa debe mostrar el costo de admisión para el grupo con un mensaje apropiado. 

El costo debe mostrarse con dos decimales.
'''

cargos = []

while True:
    edad = input("Introduzca la edad del huésped: ")

    if edad == "":
        break

    cargo = 0
    edad_int = int(edad)
    if edad_int <= 2:
        cargo = 0
    elif edad_int >= 3 and edad_int < 13:
        cargo = 14
    elif edad_int >= 65:
        cargo = 18
    else:
        cargo = 23
    cargos.append(cargo)

total = 0.00
for cargo in cargos:
    total += cargo

print("El total del grupo es:  $",(total))
