#r(lectura), 
# w(escritura)-(si no existe se crea), 
# a(añadir)-(si no existe se crea), 
# w+(escribir y leer)-(si no existe lo crea, pero si existe lo sustituye por uno nuevo), 
# r+(leer y escribir)-(si no existe da un error), 
# a+(añadir y leer)-(si no existe lo crea y si existe le añade datos al final), 
# b(para archivos binarios)-(lo abre en modo binario)
'''
Dos tipos de archivos: de texto y binarios (todo lo que no sea texto)
¿Qué se puede hacer con un archivo? open, close, read, write
    Modo de sólo lectura (r). En este caso no es posible realizar modificaciones sobre el archivo, solamente leer su contenido.
    Modo de sólo escritura (w). En este caso el archivo es truncado (vaciado) si existe, y se lo crea si no existe.
    Modo sólo escritura posicionándose al final del archivo (a). En este caso se crea el archivo, si no existe, pero en caso de que exista se posiciona al final, manteniendo el contenido original.

'''
numeros = []
ruta_base = "C:\Users\Tarde\Downloads\Tema2_Funciones\Archivos"
archivo = open(ruta_base + "\prueba.text","r") #ruta desde la raíz
for linea in archivo:
    numeros.append(int(linea))
archivo.close()
print(numeros)




