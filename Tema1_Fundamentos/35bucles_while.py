control = 0
mensaje = "ésto es un experimento de while"

while control < len(mensaje) - 1 :
    control +=1
    if mensaje[control] == "e": #se salta las e
        continue 
    print (mensaje[control])
   



''' Cosas que se puede hacer en bucles while
break:

control = 0
mensaje = "ésto es un experimento de while"

while control < 22 :
    if mensaje[control] == "x": #se detenería antes de la x de "experimento"
        break
    print (mensaje[control])
    control +=1

continue:
while control < len(mensaje) - 1 :
    control +=1
    if mensaje[control] == "e": #se salta las e al recorrerlo
        continue 
    print (mensaje[control])



exit
'''