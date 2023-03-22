def limpiar(fila):
    salida = []
    for elem in fila:
        elem = elem.replace('"','').strip() #necesario crear nueva variable, porque .replace no edita, devuelve una nueva versión
        elem.replace("\n","")
        salida.append(elem)
    return salida    


ruta_base = "C:\\Users\\Tarde\\Downloads\\Tema2_Funciones\\Archivos\\"
datos= ruta_base + "hurricanes.csv" 


huracanes = []


archivo = open(datos,"r")
cabeceras = archivo.readline()
claves = limpiar(cabeceras.split(","))


for linea in archivo:
    fila = limpiar(linea.split(","))
    d = {}
    for i in range (len(fila)):
        d[claves[i]] = fila[i]
    huracanes.append(d) 

import pprint

pprint.pprint(huracanes)



