'''
limpiar texto de signos de puntuación
eliminar palabras irrelevantes ---- menor de 3 letras
contabilizar palabras con un diccionario
devolver diccionario
'''




texto = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"


    
#1.pasar a minúscula
#2.Quitar signos de puntuación
#3.Ignorar palbras irrelevantes 
#4.Dividir la cadena por palabras
#5. Procesar la cadena

def frecuencias(text):
    salida = {}
    #1
    text = text.lower()
    #2
    puntuacion = [".",",",";",":","¡","!","¿","?","(",")"]
    for p in puntuacion:
        text = text.replace(p,"")
    palabras = text.split()
    for palabra in palabras:
        if len(palabra) >3:
            if salida.get(palabra) == None:
                salida[palabra] =1
            else: 
                salida[palabra] +=1
    return(salida)
import pprint
pprint.pprint(frecuencias(texto))




