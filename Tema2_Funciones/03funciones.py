def suma_muchos(*args): #*args ---- se le añadiran multiples valores, los que tú quieras partiendo desde 0
    total = 0
    for i in args:
        total += i
    return total

print(suma_muchos(1,2,3,4,5,6,7,8,9,12,21,21))

'''
Función que reciba como parámetro *args---- 
Concatena las cadenas contenidas en args y los separa con el separador
'''

def prueba(prueba2,*prueba3):
    pass # cuando no sabes como continuar pero quieres mantener el código mientras tanto


def encadenar(separador,*args):
    return separador.join(args)

print(encadenar("*","uduude","nd3ndujn","ojd3foijdfio3j"))


############
#Pedimos lista de cadenas
#Pedimos separador
#llamamos a encadenar 


palabras = []
while True:
    entrada = input("Dime una palabra: ")
    if entrada == "":
        break
    else:
        palabras.append(entrada)
sep = input("Dime un separador: ")
print(encadenar(sep,*palabras))



