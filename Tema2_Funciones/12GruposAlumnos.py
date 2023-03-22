import random
import pprint
alumnos = ["Javi",
"Jose",
"Miguel",
"A.Muñoz",
"Ana",
"A.Sánchez",
"Luciano",
"Juan",
"Pablo",
"Dani",
"Pedro",
"P.González",
"Carlos",
"Adrián"]

def crea_equipos(gente, miembros):
    if len(gente) < miembros:
        return (gente)
    elif miembros == 0:
        return []
    random.shuffle(gente) #baraja el parámetro gente


    num_grupos = len(gente) // miembros
    listas = []


    for i in range (num_grupos):
        equipo=[]
        for j in range (miembros):
            equipo.append(gente.pop())
        listas.append(equipo)
    
    for p in range(len(gente)):
        listas[p].append(gente[p])
    
    return listas

pprint.pprint(crea_equipos(alumnos,3))


# random.choice(gente) elige valor aleatorio






