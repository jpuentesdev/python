#las funciones deben de tener bajo acoplamiento y alta cohesión
def saludo(nombre, dia):    #nombre es el parámetro
    print(f"Buenas tardes, {nombre} hoy es {dia}")

saludo("Manolito","Lunes")   #Manolito es el argumento


#def inversa:---- recibe cadena de texto y debe imprimirlo a la inversa

def inversa(cadena):
    return(cadena[::-1])



palabras = ["uno", "dos", "tres", "cuatro"]

for p in palabras:
    x= (inversa(p))
    print(x)



#----

"""
vocales = {}

letras ="aeiou"

for c in letras:
    vocales[c] = cadena.lower().count(c) 

print(vocales)

"""
# pasando a función el script del viernes

def cuenta_vocales(cadena):
    vocales = {}
    letras = "aeiou"

    for c in letras:
        vocales[c] = cadena.lower().count(c)
    
    return vocales

texto = "Estamos orgullosos de nuestro trabajo y esperamos que disfrutes leyendo nuestros artículos. Pero además te invitamos a colaborar haciendo sugerencias o escribiendo tú mismo para mejorar los artículos que hay y crear los que faltan."

x = cuenta_vocales(texto)
print(x)

###### Reciba dos numeros y ejecute la suma

def suma(num1,num2):
    return num1 + num2

print(suma(1,4))


###### Recibe como parametro una cadena y devolverá otra cadena con ##### menos los cuatro últimos

def cifrado(cadena):
    asterisco = "*"
    return ((len(cadena) -4) * asterisco) + cadena[-4:]

print(cifrado("18487489173489734"))



############### devuelve true si contiene la letra

def contine_letra(cadena , letra):
    if letra in cadena:
        return True
    else:
        return False

print(contine_letra("holamellamox", "x"))

######### hecho por el profesor
def contine_letra(cadena , letra):
    return letra in cadena
        
    



