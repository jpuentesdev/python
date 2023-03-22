'''
Modifica el programa anterior de tal forma que los caracteres utilizados en el perímetro
del rectángulo sean caracteres producto (*) y el interior esté vacío.
'''
''' 
--- D I B U J O D E R E C T A N G U L O S ---
¿Qué dimensiones tiene el rectángulo?
- Base: 5
- Altura: 4
* * * * *
*       *
*       * 
* * * * *
'''


base = 5
altura = 4

linea_base = "*\t" * base
linea_media = "*\t" + "\t" * (base-2) + "*"

print(linea_base)
for i in range(altura -2):
    print(linea_media)

print(linea_base)











