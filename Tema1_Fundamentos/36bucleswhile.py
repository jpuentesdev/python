'''
D una lista de palabras
encontrar la más larga de la lista
'''

palabras = ["hola","adios","manzana","pera","pin"]

print(len("hola"))
print(palabras[0])

if len(palabras[0]) > len(palabras[1]) and len(palabras[0]) > len(palabras[2]) and len(palabras[0]) > len(palabras[3]) and len(palabras[0]) > len(palabras[4]):
    print ("Hola es la más larga")

elif len(palabras[1]) > len(palabras[0]) and len(palabras[1]) > len(palabras[2]) and len(palabras[1]) > len(palabras[3]) and len(palabras[1]) > len(palabras[4]):
    print ("adios es la más larga")

elif len(palabras[2]) > len(palabras[0]) and len(palabras[2]) > len(palabras[1]) and len(palabras[2]) > len(palabras[3]) and len(palabras[2]) > len(palabras[4]):
    print ("manzana es la más larga")

elif len(palabras[3]) > len(palabras[0]) and len(palabras[3]) > len(palabras[2]) and len(palabras[3]) > len(palabras[1]) and len(palabras[3]) > len(palabras[4]):
    print ("pera es la más larga")

else: 
    print ("pin es la más larga")



    
    
    