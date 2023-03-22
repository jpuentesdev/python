#r(lectura), 
# w(escritura)-(si no existe se crea), 
# a(añadir)-(si no existe se crea), 
# w+(escribir y leer)-(si no existe lo crea, pero si existe lo sustituye por uno nuevo), 
# r+(leer y escribir)-(si no existe da un error), 
# a+(añadir y leer)-(si no existe lo crea y si existe le añade datos al final), 
# b(para archivos binarios)-(lo abre en modo binario)

ruta_base = "C:\\Users\\Tarde\\Downloads\\Tema2_Funciones\\Archivos\\"
archivo= ruta_base + "datos_03.txt"

datos = [{"nombre": "Juan", "apellido1":"García","apellido2": "Romero","edad":22},
        {"nombre": "Miguelito", "apellido1":"Huevos","apellido2": "Fritos","edad":25},
        {"nombre": "Rosarito", "apellido1":"Rodríguez","apellido2": "Palermo","edad":40}
]


f = open(archivo, "w")
for d in datos: 
    cadena = f"{d["nombre"] , d["apellido1"], d["apellido2"], d["edad"]}\n"
    f.write(cadena)
f.close