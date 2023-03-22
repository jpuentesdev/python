#DICCIONARIOS

d ={
    "uno" : "Primero",
    "dos" : "Segundo",
}

print(d["uno"]) #busca la clave y devuelve el valor
d["tres"] = "Tercero" #se le añade otro valor al diccionario al diccionario(es mutable)

print(d["uno"])
print(d["dos"])
print(d["tres"])

print(d.keys()) #te devuelve todas las claves
print(d.values()) #te devuelve todos los valores

d.clear() #borra el diccionario entero
del(d["tres"]) #borra esa clave y su correspondiente valor


