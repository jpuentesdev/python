import pprint #pretty print

coches = {
    "1234FRD" : "Opel Corsa",
    "0987SDR" : "Ford Fiesta",
    "1929PLK" : "Ford Kuga"
}

print(coches) #imprime el diccionario entero
print(coches.keys()) #imprime sólo matrículas (claves)
print(coches.values()) #imprime sólo coches (valores)


coches["7777SDB"] = "Mercedes Clase A" #lo sumo al diccionario y se ejecuta en los print

print(list(coches)) #imprime una lista de sólo las claves 

pprint.pprint(coches) #imprime el diccionario formateado, en lista vertical

#INTERSANTE : encima de una función ---- control click izquierdo---- llegas al código fuente de python