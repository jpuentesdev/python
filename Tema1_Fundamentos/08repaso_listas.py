#13/10

lista = [1,2,3,4, "HOLA", True, ["a","b","c"]]
lista.append("otro")
lista.extend([7,8,9])

lista.insert(4, "nuevo dato")  #colocar nueva información emn la posición que queramos

lista= lista + ["k", "l", "m"] + [1,4,7]

x = lista.pop() #si no lo igualas a una variable, pierdes la información, ya no tienes acceso a ella
print(x)
print(lista)

#lector = lista[5]
#largo= len(lista) longitud de la lista


############## Tuplas ############################

tupla=(1,2,3,1,2,1)

largo = len(tupla)
elem = tupla.count(1)
print("Largo: ",largo)
print("Elem: ", elem)

#tupla=1, ------ se interpreta como tupla, al llevar una coma, no le hacen falta paréntesis

