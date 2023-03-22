#según notas de los alumnos --- suspenso, aprobado, notable, sobresaliente
nota = int(input("Dime tu nota: "))
if nota >= 9 and  nota<=10 :
    print("Tiene un sobresaliente")   
elif nota >= 7 and nota<= 8:
    print("Tiene un notable")
elif nota >=5 and nota<=6:
    print("Tiene un aprobado")
elif nota <5 and nota >=0:
    print("Tiene un suspenso")
else:
    print("Número no disponible")



############# Hecho por el profesor ####################


nota = int(input("Dime tu nota: "))
resultado= ""

if nota <5:
    resulado = "Suspenso"
else:
    if nota <7:
        resultado = "Aprobado"
    else:
            if nota <9:
                resultado= "Notable"
            else:
                resultado = "Sobresaliente"
print(resultado)

