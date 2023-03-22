#TIPOS DE DATOS:

#string (str)     "hola", "€~#@&%", "123"
# integer (int)    150,1,555,-15,0
# floating (float)    1.25,25.0,500.50,-95.1
# listas (lst)      ["sal",1,-3,4.5,"marte",0]
# diccionarios (dic)   {"color":"rojo", "arte":"cine"}
# tuples (tup)      ("lun","mar","mie","jue","vie") son listas pero inmutables
# sets (set)    {"a","b","c","d","e"} tiene elementos únicos
# booleanos (bool)     True, False


#NOMBRE DE VARIABLES

#Al definir una variable debemos omitir tildes y la letra "ñ"
#Los nombres de variables no pueden empezar por un número


#FORMATEAR CADENAS
'''
Cadenas literales (f-strings): a partir de Python 3.8,podemos anticipar 
la concatenación de variables anteponiendo f al string
print(f"Mi auto es {color_auto} y de matrícula {matricula}")
'''

#OPERADORES MATEMÁTICOS
'''
División:
num / num2
El cociente de una división:
num // num2
El resto de una división:
num % num2
Un número elevado a otro:
num ** num2
La raíz cuadrada de un número:
num **0.5
'''


#REDONDEO
print(round(5.56784,3)) #el segundo parámetro indica cuántos diígitos quieres a partir de la coma
print(round(123.84753453535)) #lo redondea sin parte decimal


#Programa comisiones
'''
Nota IMPORTANTE--- los imputs se almacenan de manera predeterminada como strings
'''

nombre_empleado = (input("Cuál es tu nombre: "))

ventas = int(input(f"Cuánto has vendido este mes {nombre_empleado}? "))
comision = ventas * 0.14
print(f"{nombre_empleado}, este mes has comisionado {round(comision,2)}€")
