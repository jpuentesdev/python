def alumno_notas(alumno,*asignaturas):
    print(f"El alumno {alumno} se ha matriculado de las asignaturas: ")
    print(asignaturas)

alumno_notas("Miguelito de la Roda", "Progrmación", "BD", "Sistemas")


#Forma mejorada
def alumno_notas2(alumno,*asignaturas):
    print(f"El alumno {alumno} se ha matriculado de las asignaturas: ")
    print("")
    for a in asignaturas:
        print(a)

asig = ["Progrmación", "BD", "Sistemas"]
alumno_notas2("Miguelito de la Roda", *asig)




def alumno_notas3(alumno,*asignaturas,**notas):
    print(f"El alumno {alumno} se ha matriculado de las asignaturas: ")
    print("")
    for a in asignaturas:
        print(a)
    print("")
    print("Sus notas son: ")
    for k,v in notas.items():
        print(f"{k}: {v}")
        

alumno = "Miguelito de la Roda"
asig = ["Progrmación", "BD", "Sistemas"]
notas = {"Progrmación":7, "BD":2.5, "Sistemas":5}
alumno_notas3(alumno, *asig, **notas)

