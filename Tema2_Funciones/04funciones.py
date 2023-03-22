'''
'''
def opcionales(oblig_1,oblig_2, opc1="uno", opc2="dos", *args, **kwargs): #*args(lista),    #**kwargs(diccionario)----keywords, arguments (es un parámetro opcional)
    print(kwargs)

opcionales(1,2, mates=10,lengua=2,fisica=9)