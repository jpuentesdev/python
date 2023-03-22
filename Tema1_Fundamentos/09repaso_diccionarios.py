#FORMAS DE CREAR DICCIONARIOS
#mi_dict= {}
#mi_dict= dict()
import pprint

mi_dict= {
    "1":1,
    "2":4,
    "3":9,
    "4":16,
    "5":25
}

mi_dict["6"]= 36

print (mi_dict["1"]) #imprime el valor correspondiente a esa clave

persona1 = {
    "nombre": "Paco",
    "dni": "12344567L"
}

persona2 = {
    "nombre": "Paco2",
    "dni" : "12345678L"
}

personas = {            #imprimir los dos diccionarios
    1:persona1,
    2:persona2
}


pprint.pprint(personas)