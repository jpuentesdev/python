#import os
#x = os.path.exists("no_existe.txt")  


def esto_falla():
    try:
        f = open("no_existe.txt","r")
    except Exception as e:      #Exception ---- se pone por no saber el nombre del error--- FileNotFoundError sería el error
        print(e)    #Te imprime el error
    

#--------------------------------------#

def esto_falla2():
    try:
        f = open("no_existe.txt","w+")
        print("-----------------try----------------")
    except (FileNotFoundError,FileExistsError) as e:      
        print(e)    
    else:                                      # si no ha pasado ningún error pasamos al else
        print("-----------------else----------------")
    finally:                                   # tanto si si como si no
        print("-----------------finally----------------")


def genera_error(num):
    if num <10:
        raise Exception("Error de número demasiado pequeño")            #raise = "Levantar"
    else:
        print("Funciona!!!!!!!")

try:
    genera_error(9)
except:
    exit()
