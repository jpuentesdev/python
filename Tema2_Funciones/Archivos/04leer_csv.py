import csv
import pprint
#coma separate value
ruta_base = "C:\\Users\\Tarde\\Downloads\\Python\\Tema2_Funciones\\Archivos\\"
datos= ruta_base + "hurricanes.csv" 
'''
def leer_reader(fichero):
    filas = []
    with open (fichero, "r") as csv_file:
        csvreader = csv.reader(csv_file)
        cabecera = next(csvreader)
        for f in csvreader:
            filas.append(f)
    pprint.pprint(cabecera)
    pprint.pprint(filas)

leer_reader(datos)
'''
# -------------------

def leer_dictreader(archivo):
    f = open(archivo,"r")
    lector_dict = csv.DictReader(f)
    lista_dict = list(lector_dict)
    f.close()
    pprint.pprint(lista_dict)

leer_dictreader(datos)
