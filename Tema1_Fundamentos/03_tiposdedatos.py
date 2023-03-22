#tipos mutables: listas


#tipos inmutables: cadenas, números

numero = 0
 
numero=  1 

cadena = "hola"
cadena = "adios"

#prueba

#entrada
cadena= "Esto es un experimento con cadenas"

#salida
cadena= "Esto es un EXPERIMENTO con cadenas"


cadena= 'Esto es un experimento con cadenas'
cadena_upper = cadena.upper()
print(cadena)

#Resultado.ale
cadena= 'Esto es un experimento con cadenas'
cadena = cadena.replace ("experimento","EXPERIMENTO")
print(cadena)



#RESULTADO1
cadena="Esto es un"
cadenas=" experimento"
cadenass=" con cadenas"
print(cadena+cadenas+cadenass)
cadenas=cadenas.upper()
print(cadena+cadenas+cadenass)

#RESULTADO PROFESOR
cadena="Esto es un experimento con cadenas"
palabra="experimento" #válido con cualquier palabra"
longitud=len(palabra)
pto1=cadena.find("palabra")
pto2=pto1+longitud

parte1= cadena[:pto1]
parte2= palabra.upper()
parte3= cadena[pto2:]

resultado= parte1+parte2+parte3

print(resultado)
